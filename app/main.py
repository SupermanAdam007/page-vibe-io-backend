import uvicorn
from fastapi import FastAPI

from app.routers import url, persona

app = FastAPI()
app.include_router(url.router)
app.include_router(persona.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
