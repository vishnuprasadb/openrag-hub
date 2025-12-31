from fastapi import APIRouter, Request, BackgroundTasks
from integrations.slack.service import handle_slack_ask

router = APIRouter(prefix="/slack")


@router.post("/ask")
async def slack_ask(
    request: Request,
    background_tasks: BackgroundTasks,
):
    return await handle_slack_ask(request, background_tasks)
