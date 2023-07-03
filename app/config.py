from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "PageVibe API"
    OPENAI_API_KEY: str


settings = Settings()
