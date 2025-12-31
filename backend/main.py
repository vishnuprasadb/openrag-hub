import os
import pydantic

# Patch pydantic for chromadb 0.3.x compatibility
try:
    import pydantic_settings
    # Directly assign BaseSettings to avoid triggering Pydantic V2's migration error on attribute access
    pydantic.BaseSettings = pydantic_settings.BaseSettings
except ImportError:
    pass

# Load environment variables dynamically based on APP_ENV
# Usage: APP_ENV=prod uvicorn main:app
# Default: local -> loads .env.local
from dotenv import load_dotenv

app_env = os.getenv("APP_ENV", "local")
env_file = f".env.{app_env}"

# Check if the file exists before loading to avoid silent failures if intended
if os.path.exists(env_file):
    print(f"Loading environment from {env_file}")
    load_dotenv(env_file)
else:
    print(f"Warning: {env_file} not found. Using system environment variables.")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.ask import router as ask_router
from api.slack import router as slack_router
from utils.logging import setup_logging
from config import settings

setup_logging()

app = FastAPI(title="OpenRAG-Hub")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.ALLOW_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ask_router)
app.include_router(slack_router)

@app.get("/health")
def health():
    return {"status": "ok"}
