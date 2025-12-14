# Roadmap

This roadmap outlines the planned development phases of OpenRAG-Hub.

---

## Phase 1 — Backend Foundation (Sync-first)
- FastAPI application scaffold
- Config & secrets management
- `/ask` API endpoint
- Slack `/ask` with ACK + async processing
- Dummy RAG pipeline

---

## Phase 2 — Core RAG
- Vector store abstraction
- Chroma implementation
- LLM abstraction
- OpenAI provider (sync)
- Prompt discipline

---

## Phase 3 — Web Interface
- React-based chat UI
- Query execution
- Source citation display
- Error & loading states

---

## Phase 4 — Knowledge Ingestion
- File upload support
- Text extraction & chunking
- Background ingestion
- Metadata handling

---

## Phase 5 — Google Drive Ingestion
- Drive authentication
- Recursive folder ingestion
- Error handling & retries

---

## Phase 6 — Slack Integration
- `/ask` command (update-in-place UX)
- `/upload` command
- Slack file ingestion
- Permission scopes & setup docs

---

## Phase 7 — Packaging & OSS Readiness
- Dockerfiles
- docker-compose
- Setup documentation
- Apache 2.0 license

---

## Future Enhancements
- Streaming responses
- Additional LLM providers
- Access control & auth
- Multi-tenant support

