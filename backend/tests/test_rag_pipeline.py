import pytest
from core.rag.pipeline import RAGPipeline


class FakeEmbeddings:
    def embed(self, texts):
        return [[0.1, 0.2, 0.3]]


class FakeVectorStore:
    def search(self, query_embedding, top_k):
        return [
            {
                "id": "doc1",
                "score": 0.95,
                "metadata": {"text": "Python is a programming language."},
            }
        ]


class FakeLLM:
    def generate(self, prompt):
        assert "Python is a programming language." in prompt
        return "Python is a programming language."


@pytest.mark.asyncio
async def test_rag_pipeline_happy_path():
    pipeline = RAGPipeline(
        vector_store=FakeVectorStore(),
        llm_provider=FakeLLM(),
        embeddings=FakeEmbeddings(),
    )

    result = await pipeline.run("What is Python?")

    assert "Python is a programming language" in result["answer"]
    assert len(result["sources"]) == 1
    assert result["sources"][0]["id"] == "doc1"
