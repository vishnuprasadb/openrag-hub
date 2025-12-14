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

Run the backend:

```bash
uvicorn main:app --reload
```

## Frontend Setup

```bash
cd apps/web
npm install
npm run dev
```

## Next Steps

- Upload documents
- Ask questions via Web UI
- Configure Slack integration
