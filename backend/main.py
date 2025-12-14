from fastapi import FastAPI
from api.ask import router as ask_router
from api.slack import router as slack_router
from utils.logging import setup_logging

setup_logging()

app = FastAPI(title="OpenRAG-Hub")

app.include_router(ask_router)
app.include_router(slack_router)

@app.get("/health")
def health():
    return {"status": "ok"}
