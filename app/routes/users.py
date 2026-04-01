from fastapi import APIRouter, status, Depends
from ..models.models import UserCreate, UserOut, UserLogin, TokenResponse
from ..crud import  users_crud as crud
from sqlmodel import Session
from ..database.database import get_session


router = APIRouter(prefix="/user", tags=["User"])

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def  create_user(user_data: UserCreate, session: Session = Depends(get_session)):
    return crud.create_user(session, user_data)


@router.post("/login", response_model=TokenResponse)
def authenticate_user(user_data: UserLogin, session: Session = Depends(get_session)):
    return crud.authenticate_user(session, user_data)