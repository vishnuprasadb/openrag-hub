import sys
import os

# Add the parent directory to sys.path to allow imports from core
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env.local"))

from core.ingest.chunker import TextChunker
from core.embeddings.openai import OpenAIEmbeddings
from core.vector.chroma import ChromaVectorStore


SAMPLE_DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sample_docs")

import uuid


def main():
    print("🔄 Starting ingestion demo...")

    chunker = TextChunker(chunk_size=300, overlap=50)
    embeddings = OpenAIEmbeddings()
    vector_store = ChromaVectorStore()

    for filename in os.listdir(SAMPLE_DOCS_DIR):
        file_path = os.path.join(SAMPLE_DOCS_DIR, filename)

        if not os.path.isfile(file_path):
            continue

        print(f"📄 Processing {filename}")

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        chunks = chunker.chunk(text)
        vectors = embeddings.embed(chunks)

        metadatas = []
        ids = []

        for i, chunk in enumerate(chunks):
            metadatas.append(
                {
                    "source": filename,
                    "chunk_index": i,
                    "text": chunk,
                }
            )
            ids.append(f"{filename}-{uuid.uuid4()}")

        vector_store.add_documents(
            embeddings=vectors,
            metadatas=metadatas,
            ids=ids,
        )

    print("✅ Ingestion complete!")


if __name__ == "__main__":
    main()
