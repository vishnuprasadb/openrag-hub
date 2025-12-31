import asyncio
from fastapi import Request, BackgroundTasks

from integrations.slack.verify import verify_slack_request
from integrations.slack.client import post_to_slack
from core.factory import create_rag_pipeline

rag_pipeline = create_rag_pipeline()


def _run_rag_and_respond(response_url: str, query: str):
    result = asyncio.run(rag_pipeline.run(query))

    post_to_slack(
        response_url,
        {
            "response_type": "in_channel",
            "text": result["answer"],
        },
    )


async def handle_slack_ask(
    request: Request,
    background_tasks: BackgroundTasks,
):
    body = await request.body()
    verify_slack_request(request, body)

    form = await request.form()
    query = form.get("text", "").strip()
    response_url = form.get("response_url")

    background_tasks.add_task(
        _run_rag_and_respond,
        response_url,
        query,
    )

    return {
        "response_type": "ephemeral",
        "text": "🤖 Got it! Thinking…",
    }
