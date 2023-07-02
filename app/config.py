from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    app_name: str = "PageVibe API"
    CHATGPT_API_KEY: str


settings = Settings()
