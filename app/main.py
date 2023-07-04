from logging.config import dictConfig
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import nltk
import uvicorn

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
