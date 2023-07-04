from logging.config import dictConfig
import logging

import uvicorn
from fastapi import FastAPI
import nltk

from app.config import settings
from app.models import LogConfig
from app.routers import url, persona

if settings.PROD:
    app = FastAPI(docs_url=None, redoc_url=None)
else:
    app = FastAPI()

print(f"Environment: {'Prod' if settings.PROD else 'Dev'}")

dictConfig(LogConfig().dict())
log = logging.getLogger("app")


# Check if 'punkt' is already downloaded
try:
    nltk.data.find("tokenizers/punkt")
    log.info("NLTK tokenizers/punkt was found.")
except LookupError:
    log.info("NLTK tokenizers/punkt was not found, downloading.")
    nltk.download("punkt")


app.include_router(url.router)
app.include_router(persona.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
