from fastapi import HTTPException, status
from sqlmodel import Session, select
from ..models.models import UserCreate, User, UserLogin
from ..security.security import hash_password, verify_password, create_access_token

def get_user_by_email(session: Session, email: str):
    result = session.exec(select(User).where(User.email == email)).first()
    return result

def create_user(session: Session, user_data: UserCreate):
    existing_user = get_user_by_email(session, user_data.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
    
    hashed_password = hash_password(user_data.password)
    new_user = User(
        email=user_data.email,
        hashed_password=hashed_password
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    
    return new_user


def authenticate_user(session: Session, user_data: UserLogin):
    user = get_user_by_email(session, user_data.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    verified_password = verify_password(user_data.password, user.hashed_password)
    if not verified_password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token = create_access_token(user.email)
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

