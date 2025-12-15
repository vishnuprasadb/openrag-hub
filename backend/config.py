from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "OpenRAG-Hub"
    ENV: str = "local"

    # LLM
    LLM_PROVIDER: str = "openai"
    OPENAI_API_KEY: str | None = None
    OPENAI_MODEL: str = "gpt-4o-mini"
    OPENAI_TEMPERATURE: float = 0.2

    OPENAI_EMBEDDING_MODEL: str = "text-embedding-3-small"

    # Vector DB
    VECTOR_DB: str = "chroma"
    VECTOR_DB_PATH: str = "chroma"

    # Slack
    SLACK_BOT_TOKEN: str | None = None
    SLACK_SIGNING_SECRET: str | None = None

    class Config:
        env_file = "backend/.env.local"
        extra = "ignore"


settings = Settings()

