from typing import Optional
from openai import OpenAI

from config import settings
from core.llm.base import LLMProvider


class OpenAILLMProvider(LLMProvider):
    """
    Synchronous OpenAI LLM provider.
    """

    def __init__(
        self,
        model: str = "gpt-4o-mini",
        temperature: float = 0.2,
        client: Optional[OpenAI] = None,
    ):
        if not settings.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required for OpenAI LLM provider")

        self.model = model
        self.temperature = temperature
        self.client = client or OpenAI(api_key=settings.OPENAI_API_KEY)

    def generate(self, prompt: str) -> str:
        if not prompt:
            return ""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )

        return response.choices[0].message.content.strip()
