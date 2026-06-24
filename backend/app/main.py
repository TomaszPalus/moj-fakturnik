from fastapi import FastAPI

from app.config import settings

app = FastAPI(
    title=settings.APP_NAME
)

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": settings.APP_NAME
    }