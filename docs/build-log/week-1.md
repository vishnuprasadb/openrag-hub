# Build Log — Week 1  
**Milestone:** v0.1-backend-foundation

---

## Goal

Establish a solid backend foundation for OpenRAG-Hub that can support:
- A web-based query interface
- Slack integration with strict response-time constraints
- A future RAG pipeline without refactoring

---

## Scope

The scope for Week 1 included:

- FastAPI application scaffold
- Centralized configuration and environment handling
- `/ask` API endpoint for web usage
- Slack `/ask` endpoint with immediate acknowledgment and background processing
- Sync-first RAG pipeline stub
- Initial project documentation and roadmap

---

## Key Decisions

### Sync-first RAG pipeline
We intentionally started with a synchronous RAG pipeline to reduce complexity and improve debuggability, while designing interfaces that can support streaming later.

### Slack ACK + background processing
Slack enforces a ~3 second response window for slash commands. To handle longer RAG execution times safely, Slack requests are acknowledged immediately and processed asynchronously in the background.

### Clear separation of concerns
The backend is structured to clearly separate:
- API layer
- Core RAG logic
- Utility and configuration concerns

This ensures future extensibility and clean abstractions.

---

## Outcome

At the end of Week 1:

- The backend boots successfully
- `/health` endpoint responds
- `/ask` endpoint accepts queries and returns stub responses
- Slack `/ask` endpoint responds immediately without timeouts
- Project structure and architecture are locked for future work

---

## Next Steps

- Implement real vector store integration (Chroma)
- Add real LLM provider (OpenAI)
- Replace RAG stub with real retrieval and generation logic
- Begin work on `v0.2-core-rag`
