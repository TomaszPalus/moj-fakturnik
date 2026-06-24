from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.config import settings
from app.routers.notifications import (
    router as notifications_router
)

app = FastAPI(
    title=settings.APP_NAME
)

app.include_router(notifications_router)

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": settings.APP_NAME
    }