from fastapi import APIRouter, BackgroundTasks, Request
from core.rag.pipeline import RAGPipeline

router = APIRouter()
rag = RAGPipeline()

@router.post("/slack/ask")
async def slack_ask(request: Request, bg: BackgroundTasks):
    form = await request.form()
    text = form.get("text", "")

    bg.add_task(process_slack_ask, text)

    return {
        "response_type": "ephemeral",
        "text": "🤖 Working on it..."
    }

async def process_slack_ask(text: str):
    result = await rag.run(text)
    # Slack message update will be added in Week 6
    print("Slack result:", result)
