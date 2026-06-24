from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.config import settings
from app.routers.notifications import (
    router as notifications_router
)
from app.routers.invoices import (
    router as invoices_router
)
from app.routers.companies import (
    router as companies_router
)
from app.routers.ksef_connections import (
    router as ksef_connections_router
)

app = FastAPI(
    title=settings.APP_NAME
)
app.include_router(ksef_connections_router)
app.include_router(invoices_router)
app.include_router(notifications_router)
app.include_router(companies_router)

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": settings.APP_NAME
    }