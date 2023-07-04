from urllib.parse import unquote

from fastapi import APIRouter, HTTPException
import validators

from app import constants
from app.lib.url_parse import get_rated_elements
from app.lib.chat import chat_process_url
from app.models import Persona

router = APIRouter()


@router.post("/url/process/{url}", responses={400: {"description": "Invalid URL"}})
async def process_url(url: str, persona: Persona):
    unquoted_url = unquote(url)
    url_valid = bool(validators.url(unquoted_url))

    if not url_valid:
        raise HTTPException(status_code=400, detail=f"Invalid URL: {url}")

    rated_elements = "\n".join(
        [str(x) for x in get_rated_elements(url=unquoted_url, char_limit=2500)]
    )
    result = chat_process_url(
        url=unquoted_url,
        website_text=rated_elements,
        persona=persona,
        questions=constants.predefined_questions,
        # model="gpt-4",
        debug=True,
    )

    return {
        "questions_and_answers": result,
    }


@router.get("/url/constants/")
async def values():
    return {
        "predefined_questions": constants.predefined_questions,
    }
