import hmac
import hashlib
import time
from fastapi import Request, HTTPException
from config import settings


def verify_slack_request(request: Request, body: bytes):
    timestamp = request.headers.get("X-Slack-Request-Timestamp")
    signature = request.headers.get("X-Slack-Signature")

    if not timestamp or not signature:
        raise HTTPException(status_code=400, detail="Missing Slack headers")

    if abs(time.time() - int(timestamp)) > 60 * 5:
        raise HTTPException(status_code=400, detail="Stale Slack request")

    base = f"v0:{timestamp}:{body.decode()}"

    computed = "v0=" + hmac.new(
        settings.SLACK_SIGNING_SECRET.encode(),
        base.encode(),
        hashlib.sha256,
    ).hexdigest()

    if not hmac.compare_digest(computed, signature):
        raise HTTPException(status_code=403, detail="Invalid Slack signature")
