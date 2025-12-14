from typing import List
from openai import OpenAI

from config import settings


class OpenAIEmbeddings:
    """
    OpenAI-based embeddings helper.
    """

    def __init__(
        self,
        model: str = "text-embedding-3-small",
        client: OpenAI | None = None,
    ):
        if not settings.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required for OpenAI embeddings")

        self.model = model
        self.client = client or OpenAI(api_key=settings.OPENAI_API_KEY)

    def embed(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of texts.
        """
        if not texts:
            return []

        response = self.client.embeddings.create(
            model=self.model,
            input=texts,
        )

        return [item.embedding for item in response.data]
