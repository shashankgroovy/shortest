from http import HTTPStatus
from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from shortest.app import bootload
from shortest.config import get_settings
from shortest.v1 import processor
from shortest.v1.mutator import EncoderPayload
from shortest.utils.cache import Cache

client = TestClient(bootload())
settings = get_settings()


@pytest.fixture()
def sample_payload() -> EncoderPayload:
    url = "http://example.com"
    return EncoderPayload(source_url=url)


@pytest.fixture()
def sample_payload_with_params() -> EncoderPayload:
    url = "http://example.com?foo=bar"
    return EncoderPayload(source_url=url)


@pytest.fixture()
def sample_url() -> str:
    return "http://example.com"


@pytest.fixture()
def sample_url_with_params() -> str:
    return "http://example.com?foo=bar"


@pytest.fixture()
def sample_shortend_url():
    source_url = "http://example.com"
    hex = processor._encode(source_url)
    return f"{settings.base_url}/{hex}"


@pytest.fixture()
def sample_shortend_url_with_params():
    source_url = "http://example.com?foo=bar"
    hex = processor._encode(source_url)
    print('hex', hex)
    return f"{settings.base_url}/{hex}"


def test_decode(sample_url, sample_shortend_url, monkeypatch):
    """Tests v1 decode api with a sample url that is first encoded and then
    checked for decoding"""

    # Let's monkeypatch the cache
    monkeypatch.setattr(
        Cache,
        "get",
        lambda *args, **kwargs: bytes(sample_url, encoding="utf-8"),
    )

    params = {"shortened_url": sample_shortend_url}
    res = client.get("/v1/decode", params=params)
    assert res.status_code == HTTPStatus.OK
    assert res.json()["message"] == sample_url


def test_decode_unknown(sample_shortend_url, monkeypatch):
    """Tests v1 decode api with a random url"""
    # Let's monkeypatch the cache
    monkeypatch.setattr(
        Cache,
        "get",
        lambda *args, **kwargs: None,
    )

    params = {"shortened_url": sample_shortend_url}
    res = client.get("/v1/decode", params=params)
    assert res.status_code == HTTPStatus.NOT_FOUND


def test_encode(sample_payload, sample_shortend_url, monkeypatch):
    """Tests v1 encode api with a sample payload"""
    # Let's monkeypatch the cache
    monkeypatch.setattr(
        Cache,
        "get",
        lambda *args, **kwargs: bytes(sample_shortend_url, encoding="utf-8"),
    )
    monkeypatch.setattr(Cache, "set", Mock())

    res = client.post("/v1/encode", json=sample_payload.model_dump())
    assert res.status_code == HTTPStatus.OK


def test_encode_with_params(
    sample_payload_with_params,
    sample_shortend_url_with_params,
    monkeypatch,
):
    """Tests v1 encoding api route with sample payload with query params"""

    # Let's monkeypatch the cache
    monkeypatch.setattr(
        Cache,
        "get",
        lambda *args, **kwargs: bytes(sample_shortend_url_with_params, encoding="utf-8"),
    )
    monkeypatch.setattr(Cache, "set", Mock())

    res = client.post(
        "/v1/encode", json=sample_payload_with_params.model_dump()
    )
    assert res.status_code == HTTPStatus.OK
