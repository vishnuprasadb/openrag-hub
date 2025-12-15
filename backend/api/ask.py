from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from core.factory import create_rag_pipeline

router = APIRouter()

rag_pipeline = create_rag_pipeline()

class AskRequest(BaseModel):
    query: str

@router.post("/ask")
async def ask(req: AskRequest):
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    try:
        result = await rag_pipeline.run(req.query)
        return {
            "answer": result["answer"],
            "sources": result["sources"],
        }
    except Exception as e:
        # Do not leak internals
        raise HTTPException(
            status_code=500,
            detail="Failed to process query",
        )
