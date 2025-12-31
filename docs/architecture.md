# Architecture Overview

OpenRAG-Hub is designed around a **single core RAG engine** that serves multiple interfaces.

The guiding principle is:
> **One knowledge engine, many interfaces.**

---

## High-Level Flow

User (Web UI / Slack)
↓
FastAPI Backend
↓
RAG Pipeline
↓
Vector Store + LLM



---
## Layered Architecture

OpenRAG-Hub follows a layered backend architecture to keep concerns separated
and prevent interface-specific logic from leaking into the core system.

---

## Core Components

### 1. Interfaces
- **Web UI**: Local-first React application
- **Slack**: Slash commands and file uploads

Both interfaces call the same backend APIs.

---

### 2. API Layer (FastAPI)
- Request validation
- Authentication & secrets
- Background task orchestration
- Interface-specific concerns (Slack ACKs, etc.)

---

### 3. Integration (Adapter) Layer
- Location: `backend/integrations/`
- Responsibilities:
  - Platform-specific behavior (Slack, future Discord, etc.)
  - Request verification
  - Payload parsing
  - Posting responses back to external systems

#### Slack Integration Design

Slack integration is implemented as an adapter within the backend service.

- Slack does not run as a separate service
- Slash commands are handled via HTTP endpoints
- Requests are acknowledged immediately to avoid Slack timeouts
- RAG execution happens asynchronously
- Results are posted back to Slack using the response URL

This design ensures:
- A single backend service
- No duplication of RAG logic
- Easy addition of new integrations using the same pattern

---

### 4. RAG Core
The RAG core is intentionally isolated and reusable.

Responsibilities:
- Query embedding
- Context retrieval
- Prompt construction
- Response generation

---

### 5. Ingestion Engine
Supports:
- File uploads (PDF, DOCX, TXT, etc.)
- Google Drive links (file or folder, recursive)

Steps:
1. Download / receive document
2. Extract text
3. Chunk content
4. Generate embeddings
5. Store in vector DB with metadata

---

### 6. Storage Layer
- Vector database (Chroma by default)
- Metadata stored alongside embeddings
- Pluggable via abstraction layer

---

## Sync-First, Stream-Ready Design

The system is implemented **synchronously first** for reliability and simplicity.

However:
- Interfaces
- Pipelines
- Abstractions

are all designed so streaming can be added later **without refactoring**.

---

## Docker as a Packaging Layer

Docker is used to:
- Ensure reproducibility
- Simplify OSS adoption
- Separate runtime from code

Docker is **not** required for development, but is strongly recommended for distribution.

---

## Non-Goals

- Fine-tuning models
- Real-time collaboration features
- Cloud-only deployments

These are intentionally left out to keep the project focused.

