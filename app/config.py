from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "PageVibe API"
    OPENAI_API_KEY: str
    PROD: bool = True
    origins = [
        "http://localhost:3000",
        "https://walrus-app-eogao.ondigitalocean.app"
    ]


settings = Settings()
