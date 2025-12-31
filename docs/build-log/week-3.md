# Build Log — Week 3  
**Milestone:** v0.3-user-interfaces  
**Status:** Completed

---

## Goal

Expose the core RAG system to real users via:
- A local Web UI
- Slack slash command integration

Without modifying the core RAG pipeline.

---

## Scope

The planned scope for Week 3 included:

- React-based Web UI for querying the backend
- Frontend environment configuration
- Slack `/ask` slash command
- Async-safe Slack execution
- Clear separation between API layer and integration adapters
- Documentation for Slack setup and usage

---

## Work Completed

### Web UI
- Scaffolded React app using Vite
- Implemented ask → answer flow
- Rendered answer and source attribution
- Added frontend environment configuration
- Ensured Web UI consumes backend APIs only

### Slack Integration
- Implemented Slack adapter under `backend/integrations/slack`
- Added secure request signature verification
- Implemented immediate ACK to avoid Slack timeouts
- Executed RAG pipeline asynchronously
- Posted final responses back to Slack
- Added unit tests for Slack request verification

### Architecture & Refactoring
- Clarified backend layering:
  - API layer (`backend/api`)
  - Integration adapters (`backend/integrations`)
  - Core RAG logic (`backend/core`)
- Refactored Slack logic to follow adapter pattern
- Wired Slack routes cleanly into FastAPI

### Documentation
- Updated architecture documentation to reflect adapter layering
- Added Slack setup and usage guide
- Aligned README and docs with updated repository structure

---

## Key Decisions

### Adapter-based integrations
Slack integration was implemented as an adapter inside the backend service rather than a separate application. This keeps the RAG pipeline single-source-of-truth and simplifies future integrations.

### Async-safe execution
Slack requests are acknowledged immediately, with long-running RAG execution performed in the background to comply with Slack time limits.

### Interface isolation
Web UI and Slack integrations consume the backend exclusively via HTTP APIs. No interface-specific logic exists in the core RAG layer.

---

## Outcome

At the end of Week 3:

- OpenRAG-Hub supports human interaction via Web UI and Slack
- The backend remains a single, reusable service
- Integrations are async-safe and production-aligned
- Architecture is clean, extensible, and well-documented

---

## Next Steps

- Streaming responses
- File uploads and document ingestion via UI
- Google Drive ingestion
- Observability and performance metrics
