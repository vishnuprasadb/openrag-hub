from typing import Dict, Any, List
import time

from core.vector.base import VectorStore
from core.llm.base import LLMProvider
from core.embeddings.openai import OpenAIEmbeddings
from core.rag.prompt_builder import build_prompt


class RAGPipeline:
    def __init__(
        self,
        vector_store: VectorStore,
        llm_provider: LLMProvider,
        embeddings: OpenAIEmbeddings,
        top_k: int = 5,
    ):
        self.vector_store = vector_store
        self.llm = llm_provider
        self.embeddings = embeddings
        self.top_k = top_k

    async def run(self, query: str) -> Dict[str, Any]:
        start_time = time.time()

        # 1. Embed query
        embed_start = time.time()
        query_embedding = self.embeddings.embed([query])[0]
        embed_time = time.time() - embed_start

        # 2. Retrieve documents
        retrieve_start = time.time()
        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=self.top_k,
        )
        retrieve_time = time.time() - retrieve_start

        # 3. Build prompt
        prompt = build_prompt(query, results)

        # 4. Generate answer
        llm_start = time.time()
        answer = self.llm.generate(prompt)
        llm_time = time.time() - llm_start

        total_time = time.time() - start_time

        return {
            "answer": answer,
            "sources": [
                {
                    "id": r["id"],
                    "score": r["score"],
                    "snippet": r.get("metadata", {}).get("text", ""),
                }
                for r in results
            ],
            "timings": {
                "embed": round(embed_time, 3),
                "retrieve": round(retrieve_time, 3),
                "llm": round(llm_time, 3),
                "total": round(total_time, 3),
            },
        }
