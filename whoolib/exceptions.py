"""Exception hierarchy for whoolib."""

from __future__ import annotations

from typing import Any, Optional


class WhooError(Exception):
    """Base class for every whoolib error."""


class NetworkError(WhooError):
    """Transport-level failure (DNS, TLS, timeout, connection reset)."""


class HTTPError(WhooError):
    """Non-2xx HTTP response."""

    def __init__(
        self,
        message: str,
        *,
        status_code: Optional[int] = None,
        code: Optional[str] = None,
        errors: Any = None,
        body: Any = None,
        url: Optional[str] = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.code = code
        self.errors = errors
        self.body = body
        self.url = url

    def __str__(self) -> str:  # pragma: no cover - cosmetic
        msg = self.args[0] if self.args else self.__class__.__name__
        extras = []
        if self.status_code is not None:
            extras.append(f"status={self.status_code}")
        if self.code:
            extras.append(f"code={self.code}")
        return f"{msg} ({', '.join(extras)})" if extras else str(msg)


class APIError(HTTPError):
    """4xx response with a structured error payload."""


class ValidationError(APIError):
    """400/422 - request rejected by the server."""


class AuthenticationError(APIError):
    """401 - missing/expired access token, or bad credentials."""


class PermissionDeniedError(APIError):
    """403 - authenticated but not allowed."""


class NotFoundError(APIError):
    """404 - resource does not exist (or is hidden from you)."""


class RateLimitError(APIError):
    """429 - too many requests."""

    def __init__(self, message: str, *, retry_after: Optional[float] = None, **kwargs: Any) -> None:
        super().__init__(message, **kwargs)
        self.retry_after = retry_after


class ServerError(HTTPError):
    """5xx - server-side failure."""
