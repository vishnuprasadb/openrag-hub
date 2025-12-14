# Build Log — Week 2  
**Milestone:** v0.2-core-rag  
**Status:** In Progress

---

## Goal

Begin implementation of the core RAG pipeline by locking foundational primitives:
- Interfaces
- Text chunking
- Embeddings

---

## Planned Scope

- VectorStore and LLMProvider interfaces
- Text chunker utility with tests
- OpenAI embeddings helper

---

## Work Completed (So Far)

- Defined VectorStore and LLMProvider interfaces
- Implemented configurable text chunker with unit tests
- Added OpenAI embeddings helper with mockable design

---

## Key Decisions

### Interface-first approach
All concrete implementations are built against stable interfaces to avoid refactors later in the milestone.

### Mock-friendly design
External dependencies (OpenAI) are isolated to allow fast, deterministic tests.

---

## Open Items

- Chroma VectorStore implementation
- OpenAI LLMProvider (generation)
- Core RAG pipeline wiring
- End-to-end demo and docs

---

## Next Focus

- Implement Chroma VectorStore
- Add OpenAI LLMProvider (sync)
