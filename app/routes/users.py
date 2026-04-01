from fastapi import APIRouter, status, Depends
from ..models.models import UserCreate, UserOut, UserLogin, TokenResponse, User
from ..crud import  users_crud as crud
from sqlmodel import Session
from ..database.database import get_session
from ..security.dependencies import get_current_user

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def  create_user(user_data: UserCreate, session: Session = Depends(get_session)):
    return crud.create_user(session, user_data)


@router.post("/login", response_model=TokenResponse)
def authenticate_user(user_data: UserLogin, session: Session = Depends(get_session)):
    return crud.authenticate_user(session, user_data)

@router.get("/me", response_model=UserOut)
def read_me(current_user: User = Depends(get_current_user)):
    return current_user