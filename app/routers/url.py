from urllib.parse import unquote

from fastapi import APIRouter, HTTPException
import validators

from app.config import settings
from app import models, constants
from app.lib.url_parse import get_rated_elements
from app.lib.chat import chat_process_url


router = APIRouter()


@router.post("/url/process/{url}", responses={400: {"description": "Invalid URL"}})
async def process_url(url: str):
    unquoted_url = unquote(url)
    url_valid = bool(validators.url(unquoted_url))

    if not url_valid:
        raise HTTPException(status_code=400, detail=f"Invalid URL: {url}")

    rated_elements = get_rated_elements(url=unquoted_url, char_limit=2000)
    result = chat_process_url(
        url=unquoted_url,
        website_text=rated_elements,
        persona=constants.predefined_personas[1],
        questions=constants.predefined_questions,
    )

    return {
        "questions_and_answers": result,
    }


@router.get("/url/constants/")
async def values():
    return {
        "predefined_questions": constants.predefined_questions,
    }
