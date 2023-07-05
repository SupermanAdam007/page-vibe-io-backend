from logging.config import dictConfig
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import nltk
import uvicorn

from app.config import settings
from app.models import LogConfig

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

# Check if 'vader_lexicon' is already downloaded
try:
    nltk.data.find("vader_lexicon")
    log.info("NLTK vader_lexicon was found.")
except LookupError:
    log.info("NLTK vader_lexicon was not found, downloading.")
    nltk.download("vader_lexicon")

# Check if 'vader_lexicon' is already downloaded
try:
    nltk.data.find("cmudict")
    log.info("NLTK cmudict was found.")
except LookupError:
    log.info("NLTK cmudict was not found, downloading.")
    nltk.download("cmudict")


from app.routers import url, persona, constants
app.include_router(url.router)
app.include_router(persona.router)
app.include_router(constants.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
