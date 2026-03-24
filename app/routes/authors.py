from fastapi import APIRouter, status, Depends
from ..database.models import AuthorOut, AuthorBase, AuthorWithBooks
from ..database import authors_crud as crud
from sqlmodel import Session
from ..database.database import get_session
from typing import List



router = APIRouter(prefix="/authors", tags=["Authors"])

@router.get("", response_model=list[AuthorOut])
def get_authors(*, session: Session = Depends(get_session), name: str | None = None, page: int = 1, limit: int = 5):
    return crud.get_authors(session, name, page, limit)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=AuthorOut)
def create_author(*, session: Session = Depends(get_session), auth_in: AuthorBase):
    return crud.create_author(session, auth_in)

@router.get("/{author_id}", response_model=AuthorOut)
def get_author_by_id(*, session: Session = Depends(get_session), auth_id: int): 
    return crud.get_author_by_id(session, auth_id)

@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author_by_id(*, session: Session = Depends(get_session), auth_id: int):
    return crud.delete_author_by_id(session, auth_id)

        
@router.get("/{author_id}/books", response_model=AuthorWithBooks)
def get_author_books(author_id: int, session: Session = Depends(get_session)):
    return crud.get_author_books(session, author_id)