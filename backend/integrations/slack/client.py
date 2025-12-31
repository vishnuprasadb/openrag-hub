import requests


def post_to_slack(response_url: str, payload: dict):
    requests.post(response_url, json=payload, timeout=5)
