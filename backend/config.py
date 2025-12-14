from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "OpenRAG-Hub"
    ENV: str = "local"

    # LLM
    LLM_PROVIDER: str = "openai"
    OPENAI_API_KEY: str | None = None

    # Slack
    SLACK_BOT_TOKEN: str | None = None
    SLACK_SIGNING_SECRET: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
