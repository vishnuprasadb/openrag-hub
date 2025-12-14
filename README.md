# OpenRAG-Hub

**OpenRAG-Hub** is an open-source, self-hosted Retrieval-Augmented Generation (RAG) platform that enables teams to query internal knowledge through a **Web UI** or **Slack**.

It is designed to be reusable across organizations, configurable via environment variables, and extensible without refactoring core logic.

---

## ✨ Key Features

* Retrieval-Augmented Generation (RAG)
* Web-based query interface (local-first)
* Slack integration (`/ask`, `/upload`)
* File and Google Drive ingestion
* Pluggable LLM and vector database providers
* Sync-first design, streaming-ready
* Docker support for reproducible deployment

---

## 📌 Project Status

🚧 **Actively being built in public**

You can track progress via:

* 📖 Documentation: `/docs`
* 🗺️ Roadmap: `ROADMAP.md`
* 📓 Build Log: `/docs/build-log`

---

## 🧠 Architecture Overview

OpenRAG-Hub follows a **single RAG core, multiple interfaces** design:

* Web UI and Slack share the same backend APIs
* Slack requests are acknowledged immediately and processed asynchronously
* Core RAG logic is isolated and reusable
* Configuration is entirely environment-driven

For details, see:
➡️ [`docs/architecture.md`](docs/architecture.md)

---

## 🚀 Getting Started (Local)

### Prerequisites

* Python 3.10+
* Node.js 18+
* Git

### Setup

```bash
git clone https://github.com/<your-username>/openrag-hub.git
cd openrag-hub
cp .env.example .env
```

Fill in required values in `.env`

### Run Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Health check:

```bash
GET http://localhost:8000/health
```

---

## ⚙️ Configuration

All configuration is provided via environment variables.

* No secrets are hardcoded
* `.env.example` documents all supported options
* The app fails fast if required configuration is missing

This makes the project safe for reuse in personal and company environments.

---

## 🤝 Contributing

Contributions are welcome!

Please see:
➡️ [`CONTRIBUTING.md`](CONTRIBUTING.md)

---

## 📄 License

This project is licensed under the **Apache License 2.0**.

You are free to use, modify, and distribute this project in both personal and commercial settings, subject to the terms of the license.

See the [LICENSE](./LICENSE) file for details.
