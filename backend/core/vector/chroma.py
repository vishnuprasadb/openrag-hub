from typing import List, Dict, Any
import chromadb
from chromadb.config import Settings as ChromaSettings

from core.vector.base import VectorStore


class ChromaVectorStore(VectorStore):
    """
    Local Chroma-based vector store implementation.
    """

    def __init__(
        self,
        collection_name: str = "openrag-hub",
        persist_directory: str = ".chroma",
    ):
        self.client = chromadb.Client(
            ChromaSettings(
                persist_directory=persist_directory,
                anonymized_telemetry=False,
            )
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_documents(
        self,
        embeddings: List[List[float]],
        metadatas: List[Dict[str, Any]],
        ids: List[str],
    ) -> None:
        if not embeddings:
            return

        self.collection.add(
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids,
        )

        self.persist()

    def search(
        self,
        query_embedding: List[float],
        top_k: int = 5,
    ) -> List[Dict[str, Any]]:
        if not query_embedding:
            return []

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )

        matches = []
        for idx in range(len(results["ids"][0])):
            matches.append(
                {
                    "id": results["ids"][0][idx],
                    "score": results["distances"][0][idx],
                    "metadata": results["metadatas"][0][idx],
                }
            )

        return matches

    def persist(self) -> None:
        self.client.persist()
