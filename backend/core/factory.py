from config import settings

from core.rag.pipeline import RAGPipeline
from core.vector.chroma import ChromaVectorStore
from core.llm.openai import OpenAILLMProvider
from core.embeddings.openai import OpenAIEmbeddings


def create_rag_pipeline() -> RAGPipeline:
    """
    Assemble and return a fully wired RAGPipeline.
    """

    vector_store = ChromaVectorStore(
        collection_name="openrag-hub",
        persist_directory=settings.VECTOR_DB_PATH
        if hasattr(settings, "VECTOR_DB_PATH")
        else "chroma_db",
    )

    embeddings = OpenAIEmbeddings()

    llm_provider = OpenAILLMProvider()

    return RAGPipeline(
        vector_store=vector_store,
        llm_provider=llm_provider,
        embeddings=embeddings,
    )
