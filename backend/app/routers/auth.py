from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_current_user
from app.database import SessionLocal
from app.schemas.user import UserCreate, UserLogin
from app.services.user_service import create_user, get_user_by_email
from app.services.security import hash_password, verify_password
from app.services.jwt_service import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
        
@router.get("/me")
def me(
    current_user=Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "email": current_user.email
    }

@router.get("/ping")
def ping():
    return {
        "message": "auth router works"
    }
    
@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    db_user = get_user_by_email(
        db,
        user.email
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        user.password,
        db_user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        user_id=db_user.id,
        email=db_user.email
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
    
@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    created_user = create_user(
        db=db,
        email=user.email,
        password_hash=hash_password(user.password)
    )

    return {
        "id": created_user.id,
        "email": created_user.email
    }