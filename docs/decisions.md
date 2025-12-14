# Architectural Decisions

This document captures key design decisions made during the development of OpenRAG-Hub.

---

## Sync-First RAG Pipeline

**Decision:** Start with synchronous RAG.

**Reasoning:**
- Simpler debugging
- Lower operational complexity
- Easier Slack integration

**Trade-off:**
- No token streaming initially

---

## Slack ACK + Background Processing

**Decision:** Acknowledge Slack commands immediately and process in background.

**Reasoning:**
- Slack enforces a 3-second response window
- Prevents user-facing failures

---

## Pluggable LLM & Vector Stores

**Decision:** Abstract providers from day one.

**Reasoning:**
- Avoid vendor lock-in
- Encourage OSS contributions
- Support company reuse

---

## Docker as Distribution Layer

**Decision:** Add Docker after core functionality.

**Reasoning:**
- Faster early development
- Cleaner packaging
- Lower contributor friction