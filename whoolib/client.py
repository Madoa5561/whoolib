"""HTTP client for the whoo mobile API.

This is an unofficial client reconstructed from the Android app (v0.140.0).
Use it only with your own account and in compliance with whoo's Terms of
Service and applicable law (see README.md).
"""

from __future__ import annotations

import json
import logging
import os
import threading
import time
import uuid
from typing import Any, Iterable, Mapping, Optional, Sequence
from urllib.parse import quote

import httpx

from ._endpoints import ENDPOINTS, Endpoint
from .exceptions import (
    APIError,
    AuthenticationError,
    HTTPError,
    NetworkError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    ServerError,
    ValidationError,
)
from .models import MODEL_BY_NAME, Model

__all__ = ["WhooClient"]

APP_VERSION = "0.140.0"
DEFAULT_BASE_URL = "https://www.wh00.ooo/api/"
DEFAULT_USER_AGENT = f"app.whoo/{APP_VERSION} Android/14/generic"
DEFAULT_ACCEPT_LANGUAGE = "ja"

_RETRY_STATUS = {429, 500, 502, 503, 504}
_RETRY_METHODS = {"GET", "HEAD", "PUT", "DELETE"}

log = logging.getLogger("whoolib")


class WhooClient:
    """Synchronous client for ``https://www.wh00.ooo/api/``.

    Parameters
    ----------
    access_token:
        Bearer token obtained from :meth:`login` / :meth:`register`.
    rate_limit:
        Maximum requests per second (default 3.0). Set ``0`` to disable.
    max_retries:
        Retries for idempotent requests on 429/5xx and transport errors.
    transport:
        Optional ``httpx.BaseTransport`` (used by the test-suite).
    """

    def __init__(
        self,
        base_url: str = DEFAULT_BASE_URL,
        *,
        access_token: Optional[str] = None,
        user_agent: str = DEFAULT_USER_AGENT,
        accept_language: str = DEFAULT_ACCEPT_LANGUAGE,
        timeout: float = 30.0,
        rate_limit: float = 3.0,
        max_retries: int = 2,
        transport: Optional[httpx.BaseTransport] = None,
        support_device_token: Optional[str] = None,
        verify: bool = True,
    ) -> None:
        self.base_url = base_url.rstrip("/") + "/"
        self.access_token = access_token
        self.user_agent = user_agent
        self.accept_language = accept_language
        self.timeout = timeout
        self.rate_limit = rate_limit
        self.max_retries = max(0, max_retries)
        self.support_device_token = support_device_token or str(uuid.uuid4())

        self._min_interval = (1.0 / rate_limit) if rate_limit and rate_limit > 0 else 0.0
        self._last_request = 0.0
        self._lock = threading.Lock()

        self._http = httpx.Client(
            timeout=timeout,
            transport=transport,
            verify=verify,
            follow_redirects=True,
            headers={
                "User-Agent": self.user_agent,
                "Accept-Language": self.accept_language,
                "Accept": "application/json",
            },
        )

        # Imported lazily to avoid a circular import at module load.
        from .api import API

        self.api = API(self)

    # ------------------------------------------------------------------ auth
    def login(self, email: str, password: str, *, adid: Optional[str] = None) -> Any:
        """Log in with e-mail/password.

        The real app sends ``email/login`` as ``multipart/form-data`` with the
        fields ``email``, ``password`` and ``adid`` (advertising id).
        Returns the ``UserResponse`` model (``.user`` / ``.access_token``).
        """
        parts: dict[str, Any] = {"email": email, "password": password, "adid": adid or ""}
        resp = self.call("post_email_login", parts=parts, auth=False)
        token = getattr(resp, "access_token", None)
        errors = getattr(resp, "errors", None)
        if not token and isinstance(resp, dict):
            token = resp.get("access_token")
            errors = resp.get("errors")
        if not token:
            raise AuthenticationError(
                "login response did not contain access_token",
                status_code=200,
                errors=errors,
                body=resp,
            )
        self.access_token = token
        return resp

    def register(
        self,
        *,
        display_name: str,
        birthday: str,
        username: str,
        email: str,
        password: str,
        profile_image: str = "",
        referrership_uid: Optional[str] = None,
        adid: Optional[str] = None,
    ) -> Any:
        """Create an account (``POST email/users``).

        ``birthday`` is sent as a string (the app uses ISO ``YYYY-MM-DD``).
        ``username`` is the whoo ID (``@handle`` without the ``@``).
        """
        body = {
            "display_name": display_name,
            "profile_image": profile_image,
            "birthday": birthday,
            "username": username,
            "email": email,
            "password": password,
            "referrership_uid": referrership_uid,
            "adid": adid or "",
        }
        resp = self.call("post_email_users", body=body, auth=False)
        token = getattr(resp, "access_token", None)
        if not token and isinstance(resp, dict):
            token = resp.get("access_token")
        if token:
            self.access_token = token
        return resp

    def logout(self) -> None:
        """Drop the access token locally (the API has no logout endpoint)."""
        self.access_token = None

    # --------------------------------------------------------------- helpers
    def me(self) -> Any:
        """``GET my`` - the authenticated user's profile."""
        return self.call("get_my")

    def update_location(
        self,
        latitude: float,
        longitude: float,
        *,
        speed: float = 0.0,
        accuracy: float = 0.0,
        bearing: float = 0.0,
        stayed_at: Optional[str] = None,
        location_type: int = 0,
        battery_level: float = 0.0,
        battery_state: int = 0,
        active: bool = True,
        spot_id: Optional[int] = None,
    ) -> Any:
        """``PATCH user/location`` - push the current location.

        Mirrors ``UserLocationRequestDTO`` exactly; this is the same payload
        the official app sends on every location update.
        """
        body = {
            "user_location": {
                "latitude": latitude,
                "longitude": longitude,
                "speed": speed,
                "stayed_at": stayed_at,
                "bearing": bearing,
                "horizontal_accuracy": accuracy,
                "getting_location_type": location_type,
            },
            "user_battery": {"level": battery_level, "state": battery_state},
            "app_state": {"active": active},
            "user_spot": {"id": spot_id},
        }
        return self.call("patch_user_location", body=body)

    def set_online(self) -> Any:
        return self.call("patch_user_online")

    def set_offline(self, *, parts: Optional[Mapping[str, Any]] = None) -> Any:
        """``PATCH user/offline``.

        The APK contains two variants: one with multipart device info
        (``patch_user_offline``) and a plain one (``patch_user_offline_2``).
        """
        if parts:
            return self.call("patch_user_offline", parts=parts)
        return self.call("patch_user_offline_2")

    # ------------------------------------------------------------------ core
    def call(
        self,
        name: str,
        *,
        path: Optional[Mapping[str, Any]] = None,
        query: Optional[Mapping[str, Any]] = None,
        body: Any = None,
        parts: Optional[Mapping[str, Any]] = None,
        form: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
        auth: Optional[bool] = None,
        parse: bool = True,
    ) -> Any:
        """Invoke an endpoint from :data:`whoolib._endpoints.ENDPOINTS`.

        ``body`` may be a dict or a :class:`whoolib.models.Model`.
        ``parts`` is a mapping for multipart endpoints
        (``str`` | ``bytes`` | ``(filename, bytes[, content_type])``).
        """
        ep = ENDPOINTS.get(name)
        if ep is None:
            raise KeyError(f"unknown endpoint {name!r}; see docs/ENDPOINTS.md")
        if auth is None:
            auth = ep.auth
        if auth and not self.access_token:
            raise AuthenticationError("not logged in: access_token is missing")

        url = self._build_url(ep, path or {})
        params = self._build_query(query or {})

        hdrs: dict[str, str] = {}
        if auth:
            hdrs["Authorization"] = f"Bearer {self.access_token}"
        if ep.path.startswith("support") or "/support/" in ep.path:
            hdrs["X-Whoo-Support-Device-Token"] = self.support_device_token
        if headers:
            hdrs.update(headers)

        json_body = None
        data = None
        files = None
        if parts is not None:
            files = self._build_parts(parts)
        elif form is not None:
            data = {k: v for k, v in form.items() if v is not None}
        elif body is not None:
            json_body = body.to_dict() if isinstance(body, Model) else body

        resp = self._request(
            ep.verb, url, params=params, headers=hdrs, json=json_body, data=data, files=files
        )
        return self._parse(resp, ep, parse)

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Iterable[tuple]] = None,
        json_body: Any = None,
        data: Any = None,
        files: Any = None,
        headers: Optional[Mapping[str, str]] = None,
        auth: bool = True,
        parse: bool = True,
    ) -> Any:
        """Low-level escape hatch for endpoints not present in the catalog."""
        if auth and not self.access_token:
            raise AuthenticationError("not logged in: access_token is missing")
        url = self.base_url + path.lstrip("/")
        hdrs: dict[str, str] = {}
        if auth:
            hdrs["Authorization"] = f"Bearer {self.access_token}"
        if headers:
            hdrs.update(headers)
        resp = self._request(
            method.upper(), url, params=list(params or []), headers=hdrs,
            json=json_body, data=data, files=files,
        )
        return self._parse(resp, None, parse)

    # ------------------------------------------------------------- internals
    def _build_url(self, ep: Endpoint, values: Mapping[str, Any]) -> str:
        path = ep.path
        for wire, _arg, _typ in ep.path_params:
            if wire not in values or values[wire] is None:
                raise ValueError(f"missing path parameter {wire!r} for {ep.name}")
            path = path.replace("{" + wire + "}", quote(str(values[wire]), safe=""))
        if "{" in path:
            raise ValueError(f"unresolved path template: {path}")
        base = ep.base_url or self.base_url
        if not base.endswith("/"):
            base += "/"
        return base + path

    @staticmethod
    def _build_query(values: Mapping[str, Any]) -> list[tuple[str, str]]:
        out: list[tuple[str, str]] = []
        for key, val in values.items():
            if val is None:
                continue
            if isinstance(val, (list, tuple, set)):
                for item in val:
                    if item is not None:
                        out.append((key, str(item)))
            else:
                out.append((key, str(val)))
        return out

    @staticmethod
    def _build_parts(parts: Mapping[str, Any]) -> dict[str, Any]:
        files: dict[str, Any] = {}
        for key, val in parts.items():
            if val is None:
                continue
            if isinstance(val, tuple):
                files[key] = val
            elif isinstance(val, (bytes, bytearray)):
                files[key] = (None, bytes(val), "application/octet-stream")
            else:
                files[key] = (None, str(val))
        return files

    def _throttle(self) -> None:
        if self._min_interval <= 0:
            return
        with self._lock:
            now = time.monotonic()
            wait = self._last_request + self._min_interval - now
            if wait > 0:
                time.sleep(wait)
            self._last_request = time.monotonic()

    def _request(
        self,
        method: str,
        url: str,
        *,
        params: list[tuple[str, str]],
        headers: Mapping[str, str],
        json: Any = None,
        data: Any = None,
        files: Any = None,
    ) -> httpx.Response:
        retryable = method in _RETRY_METHODS
        attempts = self.max_retries + 1
        last_exc: Optional[Exception] = None

        for attempt in range(attempts):
            self._throttle()
            try:
                resp = self._http.request(
                    method, url, params=params, headers=headers,
                    json=json, data=data, files=files,
                )
            except httpx.HTTPError as exc:
                last_exc = exc
                if retryable and attempt + 1 < attempts:
                    self._sleep_backoff(attempt)
                    continue
                raise NetworkError(f"{method} {url} failed: {exc}") from exc

            if resp.status_code in _RETRY_STATUS and retryable and attempt + 1 < attempts:
                delay = self._retry_after(resp) or (0.5 * (2 ** attempt))
                log.debug("retrying %s %s after %s (status %s)", method, url, delay, resp.status_code)
                time.sleep(delay)
                continue
            return resp

        raise NetworkError(f"{method} {url} failed after {attempts} attempts") from last_exc

    @staticmethod
    def _retry_after(resp: httpx.Response) -> Optional[float]:
        value = resp.headers.get("Retry-After")
        if not value:
            return None
        try:
            return float(value)
        except ValueError:
            return None

    @staticmethod
    def _sleep_backoff(attempt: int) -> None:
        time.sleep(0.5 * (2 ** attempt))

    def _parse(self, resp: httpx.Response, ep: Optional[Endpoint], parse: bool) -> Any:
        body: Any = None
        ctype = resp.headers.get("Content-Type", "")
        if resp.content:
            if "json" in ctype or resp.text[:1] in ("{", "["):
                try:
                    body = resp.json()
                except ValueError:
                    body = resp.text
            else:
                body = resp.text

        if resp.status_code >= 400:
            self._raise_http_error(resp, body)

        if not parse:
            return body
        if ep is not None and ep.response_model and isinstance(body, dict):
            cls = MODEL_BY_NAME.get(ep.response_model)
            if cls is not None:
                try:
                    return cls.from_dict(body)
                except TypeError:  # pragma: no cover - unexpected schema drift
                    return body
        return body

    @staticmethod
    def _raise_http_error(resp: httpx.Response, body: Any) -> None:
        code = errors = None
        message = f"HTTP {resp.status_code}"
        if isinstance(body, dict):
            code = body.get("error_code") or body.get("errorCode") or body.get("code")
            errors = body.get("errors") or body.get("error")
            if isinstance(errors, str):
                message = errors
            elif isinstance(errors, list) and errors:
                message = "; ".join(str(e) for e in errors[:3])
            elif isinstance(body.get("message"), str):
                message = body["message"]
        elif isinstance(body, str) and body:
            message = body[:300]

        kwargs = dict(status_code=resp.status_code, code=code, errors=errors,
                      body=body, url=str(resp.request.url))
        status = resp.status_code
        if status in (400, 422):
            raise ValidationError(message, **kwargs)
        if status == 401:
            raise AuthenticationError(message, **kwargs)
        if status == 403:
            raise PermissionDeniedError(message, **kwargs)
        if status == 404:
            raise NotFoundError(message, **kwargs)
        if status == 429:
            retry_after = WhooClient._retry_after(resp)
            raise RateLimitError(message, retry_after=retry_after, **kwargs)
        if status >= 500:
            raise ServerError(message, **kwargs)
        raise APIError(message, **kwargs)

    # ------------------------------------------------------------- sessions
    def export_session(self) -> dict:
        """Return a JSON-serialisable session dict (contains the bearer token)."""
        return {
            "base_url": self.base_url,
            "access_token": self.access_token,
            "user_agent": self.user_agent,
            "accept_language": self.accept_language,
            "support_device_token": self.support_device_token,
        }

    def save_session(self, path: str) -> None:
        """Write the session to ``path`` (plaintext; keep the file private)."""
        data = json.dumps(self.export_session(), ensure_ascii=False, indent=2)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(data)
        try:
            os.chmod(path, 0o600)
        except OSError:  # pragma: no cover - Windows / restricted FS
            pass

    @classmethod
    def from_session(cls, path: str, **kwargs: Any) -> "WhooClient":
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        kwargs.setdefault("base_url", data.get("base_url", DEFAULT_BASE_URL))
        kwargs.setdefault("user_agent", data.get("user_agent", DEFAULT_USER_AGENT))
        kwargs.setdefault("accept_language", data.get("accept_language", DEFAULT_ACCEPT_LANGUAGE))
        kwargs.setdefault("support_device_token", data.get("support_device_token"))
        return cls(access_token=data.get("access_token"), **kwargs)

    # -------------------------------------------------------------- lifecycle
    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> "WhooClient":
        return self

    def __exit__(self, *exc_info: Any) -> None:
        self.close()
