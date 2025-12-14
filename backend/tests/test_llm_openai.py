import pytest
from core.llm.openai import OpenAILLMProvider, settings


class FakeMessage:
    def __init__(self, content):
        self.content = content


class FakeChoice:
    def __init__(self, content):
        self.message = FakeMessage(content)


class FakeResponse:
    def __init__(self, content):
        self.choices = [FakeChoice(content)]


class FakeChatCompletions:
    @staticmethod
    def create(model, temperature, messages):
        return FakeResponse("hello from fake llm")


class FakeOpenAIClient:
    def __init__(self):
        self.chat = type(
            "chat",
            (),
            {"completions": FakeChatCompletions()},
        )


def test_generate_text(monkeypatch):
    monkeypatch.setattr(settings, "OPENAI_API_KEY", "test-key")

    llm = OpenAILLMProvider(client=FakeOpenAIClient())
    output = llm.generate("Hello")

    assert output == "hello from fake llm"


def test_empty_prompt(monkeypatch):
    monkeypatch.setattr(settings, "OPENAI_API_KEY", "test-key")

    llm = OpenAILLMProvider(client=FakeOpenAIClient())
    assert llm.generate("") == ""

def test_empty_api_key(monkeypatch):
    monkeypatch.setattr(settings, "OPENAI_API_KEY", None)

    with pytest.raises(ValueError):
        OpenAILLMProvider()
