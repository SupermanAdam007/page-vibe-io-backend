from urllib.parse import unquote

from fastapi import FastAPI, HTTPException
import validators

from config import settings


app = FastAPI()


@app.get("/urlsubmit/{url}")
async def urlsubmit(url: str):
    unquoted_url = unquote(url)
    url_valid = bool(validators.url(unquoted_url))

    if not url_valid:
        raise HTTPException(status_code=400, detail="URL is not valid")

    return {"message": f"url: {unquoted_url}", "url_valid": url_valid, "CHATGPT_API_KEY": settings.CHATGPT_API_KEY}
