"""Tests for whoolib (offline, using httpx.MockTransport)."""

from __future__ import annotations

import json

import httpx
import pytest

from whoolib import (
    AuthenticationError,
    RateLimitError,
    ValidationError,
    WhooClient,
)
from whoolib._endpoints import ENDPOINTS
from whoolib.models import MODEL_BY_NAME

USER = {
    "id": 1,
    "uid": "abc",
    "display_name": "tester",
    "profile_image": "https://example.invalid/a.png",
}


def make_client(handler, **kwargs):
    return WhooClient(transport=httpx.MockTransport(handler), rate_limit=0, **kwargs)


def test_catalog_is_complete_and_consistent():
    assert len(ENDPOINTS) == 213
    from collections import Counter

    verbs = Counter(e.verb for e in ENDPOINTS.values())
    assert verbs == {"GET": 115, "POST": 58, "PATCH": 21, "DELETE": 17, "PUT": 2}
    names = [e.name for e in ENDPOINTS.values()]
    assert len(names) == len(set(names))
    for ep in ENDPOINTS.values():
        for wire, _arg, _type in ep.path_params:
            assert "{" + wire + "}" in ep.path, (ep.name, wire)
        # every placeholder has a parameter
        import re

        placeholders = set(re.findall(r"\{([^}]+)\}", ep.path))
        assert placeholders == {w for w, _a, _t in ep.path_params}, ep.name


def test_login_sends_multipart_and_stores_token():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["method"] = request.method
        seen["url"] = str(request.url)
        seen["content_type"] = request.headers.get("content-type", "")
        seen["body"] = request.read()
        return httpx.Response(200, json={"user": USER, "access_token": "tok-123"})

    client = make_client(handler)
    resp = client.login("a@example.com", "secret", adid="adid-1")

    assert seen["method"] == "POST"
    assert seen["url"].endswith("/api/email/login")
    assert seen["content_type"].startswith("multipart/form-data")
    assert b'name="email"' in seen["body"]
    assert b"a@example.com" in seen["body"]
    assert b'name="password"' in seen["body"]
    assert b'name="adid"' in seen["body"]
    assert client.access_token == "tok-123"
    assert getattr(resp, "access_token") == "tok-123"
    assert resp.user["display_name"] == "tester"


def test_login_without_token_raises():
    def handler(request):
        return httpx.Response(200, json={"user": USER, "errors": ["invalid"]})

    client = make_client(handler)
    with pytest.raises(AuthenticationError):
        client.login("a@example.com", "secret")


def test_auth_header_and_model_parsing():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["auth"] = request.headers.get("authorization")
        seen["ua"] = request.headers.get("user-agent")
        seen["lang"] = request.headers.get("accept-language")
        return httpx.Response(200, json={"user": USER})

    client = make_client(handler)
    client.access_token = "tok"
    me = client.me()

    assert seen["auth"] == "Bearer tok"
    assert seen["ua"].startswith("app.whoo/0.140.0")
    assert seen["lang"] == "ja"
    assert me.user["id"] == 1


def test_missing_token_blocks_authenticated_call():
    client = make_client(lambda request: httpx.Response(200, json={}))
    with pytest.raises(AuthenticationError):
        client.call("get_my")


def test_update_location_payload():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["url"] = str(request.url)
        seen["method"] = request.method
        seen["json"] = json.loads(request.read())
        return httpx.Response(200, json={"updating": True})

    client = make_client(handler)
    client.access_token = "tok"
    client.update_location(35.68, 139.76, accuracy=5.0, battery_level=0.8, spot_id=9)

    assert seen["method"] == "PATCH"
    assert seen["url"].endswith("/api/user/location")
    body = seen["json"]
    assert body["user_location"]["latitude"] == 35.68
    assert body["user_location"]["longitude"] == 139.76
    assert body["user_location"]["horizontal_accuracy"] == 5.0
    assert body["user_battery"] == {"level": 0.8, "state": 0}
    assert body["app_state"] == {"active": True}
    assert body["user_spot"] == {"id": 9}


def test_path_and_query_parameters():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["url"] = str(request.url)
        return httpx.Response(200, json={})

    client = make_client(handler)
    client.access_token = "tok"
    client.api.get_rooms_id_users(7, page=2, state="active")

    assert "/api/rooms/7/users" in seen["url"]
    assert "page=2" in seen["url"]
    assert "state=active" in seen["url"]


def test_validation_error_mapping():
    def handler(request):
        return httpx.Response(
            422,
            json={"error_code": "validation_error", "errors": ["email is invalid"]},
        )

    client = make_client(handler)
    with pytest.raises(ValidationError) as exc:
        client.call("post_validate_email", form={"email": "x"})
    assert exc.value.status_code == 422
    assert exc.value.code == "validation_error"
    assert "email is invalid" in str(exc.value)


def test_rate_limit_error_mapping():
    def handler(request):
        return httpx.Response(429, headers={"Retry-After": "2"}, json={"errors": ["slow down"]})

    client = make_client(handler, max_retries=0)
    client.access_token = "tok"
    with pytest.raises(RateLimitError) as exc:
        client.call("get_my")
    assert exc.value.retry_after == 2.0


def test_model_roundtrip():
    cls = MODEL_BY_NAME["UserAccount"]
    account = cls(display_name="n", email="e", password="p")
    assert account.to_dict() == {"display_name": "n", "email": "e", "password": "p"}
    assert cls.from_dict({"display_name": "n"}).display_name == "n"


def test_session_roundtrip():
    path = "tests/.session.json"
    client = make_client(lambda request: httpx.Response(200, json={}))
    client.access_token = "tok"
    try:
        client.save_session(path)

        loaded = WhooClient.from_session(
            path, transport=httpx.MockTransport(lambda r: httpx.Response(200, json={}))
        )
        assert loaded.access_token == "tok"
        assert loaded.base_url == client.base_url
        assert loaded.user_agent == client.user_agent
    finally:
        import os

        if os.path.exists(path):
            os.remove(path)


def test_register_json_payload():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["url"] = str(request.url)
        seen["json"] = json.loads(request.read())
        return httpx.Response(200, json={"user": USER, "access_token": "tok"})

    client = make_client(handler)
    client.register(
        display_name="n",
        birthday="1995-04-01",
        username="tester_01",
        email="a@example.com",
        password="secret",
        referrership_uid="ref",
    )
    assert seen["url"].endswith("/api/email/users")
    assert seen["json"]["username"] == "tester_01"
    assert seen["json"]["birthday"] == "1995-04-01"
    assert seen["json"]["referrership_uid"] == "ref"
    assert seen["json"]["adid"] == ""
    assert client.access_token == "tok"


def test_base_url_override_for_spotify_endpoint():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["url"] = str(request.url)
        seen["cookie"] = request.headers.get("cookie")
        return httpx.Response(200, json={"access_token": "s"})

    client = make_client(handler)
    client.call(
        "get_api_token",
        query={"reason": "transport", "productType": "premium"},
        headers={"Cookie": "sp_dc=abc"},
    )
    assert seen["url"].startswith("https://open.spotify.com/api/token")
    assert seen["cookie"] == "sp_dc=abc"


def test_list_query_parameters_are_repeated():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["url"] = str(request.url)
        return httpx.Response(200, json={})

    client = make_client(handler)
    client.access_token = "tok"
    client.call(
        "delete_rooms_id_users_delete",
        path={"id": 1},
        query={"user_ids[]": [2, 3]},
    )
    assert "user_ids%5B%5D=2" in seen["url"]
    assert "user_ids%5B%5D=3" in seen["url"]


def test_set_offline_uses_plain_variant():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["url"] = str(request.url)
        return httpx.Response(200)

    client = make_client(handler)
    client.access_token = "tok"
    client.set_offline()
    assert seen["url"].endswith("/api/user/offline")
