import time
import hmac
import hashlib
import pytest
from fastapi import Request
from starlette.datastructures import Headers

from integrations.slack.verify import verify_slack_request
from config import settings


class FakeRequest(Request):
    def __init__(self, headers: dict):
        scope = {
            "type": "http",
            "headers": Headers(headers).raw,
            "method": "POST",
            "path": "/slack/ask",
        }
        super().__init__(scope)


def _sign(body: bytes, timestamp: str, secret: str) -> str:
    base = f"v0:{timestamp}:{body.decode()}"
    digest = hmac.new(
        secret.encode(),
        base.encode(),
        hashlib.sha256,
    ).hexdigest()
    return f"v0={digest}"

def test_valid_slack_request(monkeypatch):
    secret = "test-secret"
    monkeypatch.setattr(settings, "SLACK_SIGNING_SECRET", secret)

    body = b"token=test&text=hello"
    timestamp = str(int(time.time()))
    signature = _sign(body, timestamp, secret)

    headers = {
        "X-Slack-Request-Timestamp": timestamp,
        "X-Slack-Signature": signature,
    }

    request = FakeRequest(headers)

    # Should not raise
    verify_slack_request(request, body)

def test_invalid_signature(monkeypatch):
    monkeypatch.setattr(settings, "SLACK_SIGNING_SECRET", "correct-secret")

    body = b"text=hello"
    timestamp = str(int(time.time()))

    headers = {
        "X-Slack-Request-Timestamp": timestamp,
        "X-Slack-Signature": "v0=invalid",
    }

    request = FakeRequest(headers)

    with pytest.raises(Exception):
        verify_slack_request(request, body)

def test_stale_timestamp(monkeypatch):
    secret = "test-secret"
    monkeypatch.setattr(settings, "SLACK_SIGNING_SECRET", secret)

    body = b"text=hello"
    timestamp = str(int(time.time()) - 60 * 10)  # 10 minutes ago
    signature = _sign(body, timestamp, secret)

    headers = {
        "X-Slack-Request-Timestamp": timestamp,
        "X-Slack-Signature": signature,
    }

    request = FakeRequest(headers)

    with pytest.raises(Exception):
        verify_slack_request(request, body)

def test_missing_headers():
    request = FakeRequest({})
    with pytest.raises(Exception):
        verify_slack_request(request, b"test")

