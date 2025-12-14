from abc import ABC, abstractmethod
from typing import List, Dict, Any


class VectorStore(ABC):
    """
    Abstract interface for vector storage backends.
    """

    @abstractmethod
    def add_documents(
        self,
        embeddings: List[List[float]],
        metadatas: List[Dict[str, Any]],
        ids: List[str],
    ) -> None:
        """
        Add embedded documents to the vector store.

        Args:
            embeddings: List of embedding vectors
            metadatas: Arbitrary metadata per document
            ids: Stable unique IDs for documents
        """
        pass

    @abstractmethod
    def search(
        self,
        query_embedding: List[float],
        top_k: int = 5,
    ) -> List[Dict[str, Any]]:
        """
        Search for similar documents.

        Returns:
            List of results containing:
            - id
            - score
            - metadata
        """
        pass

    @abstractmethod
    def persist(self) -> None:
        """
        Persist data to disk if supported.
        """
        pass
