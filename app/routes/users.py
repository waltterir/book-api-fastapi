from fastapi import APIRouter, status, Depends
from ..models.models import UserCreate, UserOut
from ..crud import  users_crud as crud
from sqlmodel import Session
from ..database.database import get_session


router = APIRouter(prefix="/user", tags=["User"])

@router.post("/register", status_code=201, response_model=UserOut)
def  create_user(user_data: UserCreate, session: Session = Depends(get_session)):
    return crud.create_user(user_data, session)
