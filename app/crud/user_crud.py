from fastapi import HTTPException, Response, status
from sqlmodel import Session, select
from ..models.models import UserCreate, User
from security import hash_password

def get_user_by_email(session: Session, email: str):
    result = session.exec(select(User).where(User.email == email)).first()
    return result

def create_user(session: Session, user_data: UserCreate):
    existing_user = get_user_by_email(session, user_data.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Email already registered")
    
    hashed_password = hash_password(user_data.password)
    new_user = User(
        email=user_data.email,
        hashed_password=hashed_password
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    
    return new_user
