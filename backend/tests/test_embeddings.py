import pytest
from core.embeddings.openai import OpenAIEmbeddings, settings


class FakeEmbedding:
    def __init__(self, embedding):
        self.embedding = embedding


class FakeResponse:
    def __init__(self, data):
        self.data = data


class FakeOpenAIClient:
    class embeddings:
        @staticmethod
        def create(model, input):
            return FakeResponse(
                [FakeEmbedding([0.1, 0.2, 0.3]) for _ in input]
            )


def test_empty_input(monkeypatch):
    monkeypatch.setattr(settings, "OPENAI_API_KEY", "test-key")
    embeddings = OpenAIEmbeddings(client=FakeOpenAIClient())
    assert embeddings.embed([]) == []


def test_embeddings_shape(monkeypatch):
    monkeypatch.setattr(settings, "OPENAI_API_KEY", "test-key")

    embeddings = OpenAIEmbeddings(client=FakeOpenAIClient())
    vectors = embeddings.embed(["hello", "world"])

    assert len(vectors) == 2
    assert all(len(v) == 3 for v in vectors)
