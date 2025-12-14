# Build Log — Week 1

## Goal
Establish the backend foundation and project structure.

---

## Scope
- FastAPI app scaffold
- Config & secrets handling
- `/ask` API contract
- Slack `/ask` (ACK + background task)
- Dummy RAG pipeline

---

## Key Decisions
- Sync-first RAG
- Slack handled asynchronously at the interface level
- Clear separation between API, core, and integrations

---

## Outcome
- Backend boots successfully
- Endpoints are reachable
- Architecture is locked for future work

---

## Next
- Implement real vector store
- Add real LLM integration
