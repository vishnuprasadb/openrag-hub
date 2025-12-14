from typing import List


class TextChunker:
    """
    Simple character-based text chunker with overlap.
    """

    def __init__(self, chunk_size: int = 500, overlap: int = 50):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be > 0")
        if overlap < 0:
            raise ValueError("overlap must be >= 0")
        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size")

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str) -> List[str]:
        """
        Split text into chunks with optional overlap.

        Args:
            text: Input text

        Returns:
            List of text chunks
        """
        if not text:
            return []

        chunks: List[str] = []
        start = 0
        length = len(text)

        while start < length:
            end = start + self.chunk_size
            chunk = text[start:end]
            chunks.append(chunk)

            # Move start forward, respecting overlap
            start = end - self.overlap

            if start < 0:
                start = 0

        return chunks
