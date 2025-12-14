from unittest.mock import MagicMock, patch
from core.vector.chroma import ChromaVectorStore


@patch("core.vector.chroma.chromadb")
def test_chroma_add_and_search(mock_chromadb, tmp_path):
    # Setup mocks
    mock_client = MagicMock()
    mock_collection = MagicMock()
    mock_chromadb.Client.return_value = mock_client
    mock_client.get_or_create_collection.return_value = mock_collection
    
    # Mock search results
    mock_collection.query.return_value = {
        "ids": [["doc1"]],
        "distances": [[0.1]],
        "metadatas": [[{"text": "hello"}]],
    }

    store = ChromaVectorStore(
        collection_name="test-collection",
        persist_directory=str(tmp_path),
    )

    embeddings = [
        [0.1, 0.2, 0.3],
        [0.9, 0.8, 0.7],
    ]

    metadatas = [
        {"text": "hello"},
        {"text": "world"},
    ]

    ids = ["doc1", "doc2"]

    store.add_documents(embeddings, metadatas, ids)

    # Verify add was called
    mock_collection.add.assert_called_once_with(
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids,
    )
    
    # Verify persist
    mock_client.persist.assert_called_once()

    results = store.search([0.1, 0.2, 0.3], top_k=1)

    assert len(results) == 1
    assert results[0]["id"] == "doc1"
    assert results[0]["score"] == 0.1
