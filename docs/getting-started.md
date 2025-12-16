# Getting Started

This guide helps you run OpenRAG-Hub locally.

---

## Prerequisites

- Python 3.10+
- Node.js 18+
- Git
- OpenAI API key

---

## Clone the Repository

```bash
git clone https://github.com/<your-username>/openrag-hub.git
cd openrag-hub
```


## Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create .env from .env.example and add required keys.
Add in the required keys in the .env file.

OpenRAG-Hub includes a small set of sample documents and an ingestion script.
Run the ingestion script to add the sample documents to the vector store.

```bash
python scripts/ingest_demo.py
```

Run the backend:

```bash
uvicorn main:app --reload
```

Verify the backend is running by accessing http://localhost:8000/health in your browser.

Expected Response:

```json
{
    "status": "ok"
}
```

Now hit a real api using the below CURL.

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"query":"What is OpenRAG-Hub?"}'

```

Example Response

```json
{
  "answer": "OpenRAG-Hub is an open-source Retrieval-Augmented Generation platform.",
  "sources": [
    {
      "id": "openrag.txt-...",
      "score": 0.12,
      "snippet": "OpenRAG-Hub is an open-source Retrieval-Augmented Generation platform..."
    }
  ]
}

```

### Resetting the Vector Store (Optional)
To re-ingest documents from scratch:

```bash
rm -rf backend/.chroma_db
python scripts/ingest_demo.py
```

---

## Frontend Setup

```bash
cd apps/web
npm install
npm run dev
```

## Next Steps

- Upload documents to backend/sample_docs
- Ask questions via Web UI
- Configure Slack integration
- Swap LLMs or vector databases via configuration
