from abc import ABC, abstractmethod


class LLMProvider(ABC):
    """
    Abstract interface for LLM providers.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a response from the LLM.

        Args:
            prompt: Fully constructed prompt string

        Returns:
            Generated text response
        """
        pass
