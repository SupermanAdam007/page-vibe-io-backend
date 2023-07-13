import logging
from typing import List
from urllib.parse import unquote

from fastapi import APIRouter, HTTPException
import validators

from app.config import settings
from app.lib.chat import chat_process_url
from app.lib.text_analysis import get_text_sentiment, get_text_readibility_and_complexity
from app.lib.url_parse import get_rated_elements
from app.models import Persona, SubmitUrlRequest

router = APIRouter()

log = logging.getLogger("app")


@router.post("/url/process/", responses={
    400: {"description": "Invalid request"},
    406: {"description": "Unable to read URL"}
})
async def process_url(data: SubmitUrlRequest):
    persona: Persona = data.persona
    questions: List[str] = data.questions
    url: str = data.url
    unquoted_url = unquote(url)

    url_valid = bool(validators.url(unquoted_url))

    if not url_valid:
        raise HTTPException(status_code=400, detail=f"Invalid URL: {unquoted_url}")

    log.info(f"Processing url: {unquoted_url}")

    rated_elements = "\n".join(
        [str(x) for x in get_rated_elements(url=unquoted_url, char_limit=2500)]
    )

    if not rated_elements:
        raise HTTPException(status_code=406, detail=f"Unable to read URL: {unquoted_url}")

    result = chat_process_url(
        url=unquoted_url,
        website_text=rated_elements,
        persona=persona,
        questions=questions,
        # model="gpt-4",
        debug=settings.DEBUG,
    )

    readibility, complexity = get_text_readibility_and_complexity(rated_elements)

    return {
        "answers": result,
        "sentiment_score": get_text_sentiment(result),
        "readibility": readibility,
        "complexity": complexity,
    }
