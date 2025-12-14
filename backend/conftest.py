import sys
import os
import pydantic

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Set dummy env vars to avoid chromadb validation errors (Pydantic V2 strictness)
os.environ["CLICKHOUSE_HOST"] = "localhost"
os.environ["CLICKHOUSE_PORT"] = "8123"
os.environ["CHROMA_SERVER_HOST"] = "localhost"
os.environ["CHROMA_SERVER_HTTP_PORT"] = "8000"
os.environ["CHROMA_SERVER_GRPC_PORT"] = "50051"
os.environ["CHROMA_API_IMPL"] = "local"
os.environ["CHROMA_DB_IMPL"] = "duckdb+parquet"


# Patch pydantic for chromadb 0.3.x compatibility
try:
    import pydantic_settings
    # Directly assign BaseSettings to avoid triggering Pydantic V2's migration error on attribute access
    pydantic.BaseSettings = pydantic_settings.BaseSettings
except ImportError:
    pass
