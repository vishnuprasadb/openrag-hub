import httpx


async def post_to_slack(response_url: str, payload: dict):
    async with httpx.AsyncClient(timeout=5) as client:
        await client.post(response_url, json=payload)
