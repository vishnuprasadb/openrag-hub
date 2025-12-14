import pytest
from core.ingest.chunker import TextChunker


def test_empty_text():
    chunker = TextChunker()
    assert chunker.chunk("") == []


def test_single_chunk():
    text = "hello world"
    chunker = TextChunker(chunk_size=50, overlap=10)
    chunks = chunker.chunk(text)

    assert len(chunks) == 1
    assert chunks[0] == text


def test_multiple_chunks_no_overlap():
    text = "abcdefghijklmnopqrstuvwxyz"
    chunker = TextChunker(chunk_size=10, overlap=0)
    chunks = chunker.chunk(text)

    assert chunks == [
        "abcdefghij",
        "klmnopqrst",
        "uvwxyz",
    ]


def test_multiple_chunks_with_overlap():
    text = "abcdefghijklmnopqrstuvwxyz"
    chunker = TextChunker(chunk_size=10, overlap=2)
    chunks = chunker.chunk(text)

    assert chunks == [
        "abcdefghij",
        "ijklmnopqr",
        "qrstuvwxyz",
        "yz",
    ]

def test_overlap_is_respected():
    text = "abcdefghijklmnopqrstuvwxyz"
    chunker = TextChunker(chunk_size=10, overlap=2)
    chunks = chunker.chunk(text)

    assert chunks[0][-2:] == chunks[1][:2]

def test_invalid_chunk_size():
    with pytest.raises(ValueError):
        TextChunker(chunk_size=0, overlap=0)


def test_invalid_overlap():
    with pytest.raises(ValueError):
        TextChunker(chunk_size=10, overlap=10)
