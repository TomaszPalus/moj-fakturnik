from sqlalchemy.orm import Session
from app.models.user import User
from passlib.context import CryptContext

# password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(
    db: Session,
    email: str,
    password_hash: str
):
    user = User(
        email=email,
        password_hash=password_hash
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_user_by_email(
    db,
    email: str
):
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )
    
def verify_password(
    password: str,
    hashed_password: str
):
    return pwd_context.verify(
        password,
        hashed_password
    )
    
def get_user_by_id(
    db,
    user_id: int
):
    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )