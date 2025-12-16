# Build Log — Week 2  
**Milestone:** v0.2-core-rag  
**Status:** Completed

---

## Goal

Implement a fully functional, synchronous core RAG pipeline that can:
- Ingest documents
- Retrieve relevant context
- Generate grounded answers
- Be reused across interfaces (Web, Slack)

---

## Scope

The scope for Week 2 included:

- Vector store abstraction and local Chroma implementation
- OpenAI-based embeddings helper
- OpenAI-based synchronous LLM provider
- Core RAG pipeline (embed → retrieve → prompt → generate)
- Wiring `/ask` API endpoint to the real pipeline
- Sample documents and ingestion demo
- End-to-end reproducible local demo
- Unit tests for core helpers and pipeline wiring

---

## Work Completed

- Implemented `VectorStore` and `LLMProvider` abstractions
- Added local Chroma-based vector store with persistence
- Added OpenAI embeddings helper with mockable design
- Added synchronous OpenAI LLM provider
- Implemented core RAG pipeline with timing metrics
- Wired `/ask` endpoint to real pipeline
- Added sample documents and ingestion demo script
- Added unit tests for:
  - Chunker
  - Embeddings helper
  - LLM provider
  - Core RAG pipeline
- Documented end-to-end local setup and demo steps

---

## Key Decisions

### Interface-first design
All core components were implemented against stable interfaces to avoid refactors and enable future provider swaps.

### Sync-first pipeline
The RAG pipeline is synchronous for simplicity and debuggability, while keeping the architecture ready for streaming in future milestones.

### Mock-friendly testing
External dependencies (OpenAI, Chroma) were isolated to allow fast, deterministic unit tests without network calls.

---

## Outcome

At the end of Week 2:

- OpenRAG-Hub supports a complete end-to-end RAG flow
- Documents can be ingested locally
- `/ask` returns grounded answers with source attribution
- The system is demoable and reproducible by new users
- Core architecture is locked and extensible

---

## Next Steps

- Web UI for interactive querying
- Slack message updates for async responses
- Advanced ingestion pipelines (Drive, uploads)
- Streaming responses and observability

