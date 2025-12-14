from fastapi import APIRouter
from pydantic import BaseModel
from core.rag.pipeline import RAGPipeline

router = APIRouter()
rag = RAGPipeline()

class AskRequest(BaseModel):
    query: str

@router.post("/ask")
async def ask(req: AskRequest):
    return await rag.run(req.query)
