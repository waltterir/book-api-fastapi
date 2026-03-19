from fastapi import APIRouter, status, Depends
from ..database.models import AuthorOut, AuthorBase
from ..database import authors_crud as crud
from sqlmodel import Session
from ..database.database import get_session



router = APIRouter(prefix="/authors", tags=["Authors"])

@router.get("", response_model=list[AuthorOut])
def get_authors(*, session: Session = Depends(get_session), author: str | None = None):
    return crud.get_authors(session, author)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=AuthorOut)
def create_new_author(*, session: Session = Depends(get_session), auth_in: AuthorBase):
    return crud.create_new_author(session, auth_in)

@router.get("/{author_id}", response_model=AuthorOut)
def get_author_by_id(*, session: Session = Depends(get_session), auth_id: int): 
    return crud.get_author_by_id(session, auth_id)

@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author_by_id(*, session: Session = Depends(get_session), auth_id: int):
    return crud.delete_author_by_id(session, auth_id)