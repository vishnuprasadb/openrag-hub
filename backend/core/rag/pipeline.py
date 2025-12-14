# Dummy RAG Pipeline (Sync-First)
class RAGPipeline:
    async def run(self, query: str) -> dict:
        # Dummy response for Week 1
        return {
            "answer": f"(stub) Answer for: {query}",
            "sources": []
        }
