from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPBearer

from app.core.database import SessionLocal
from app.services.jwt_service import decode_access_token
from app.services.user_service import get_user_by_id


security = HTTPBearer()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_current_user(
    credentials=Depends(security),
    db=Depends(get_db)
):
    token = credentials.credentials

    payload = decode_access_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = get_user_by_id(
        db,
        int(payload["sub"])
    )

    return user