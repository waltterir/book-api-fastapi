from fastapi import APIRouter, status
from ..database.models import AuthorOut, AuthorBase
from ..database import authors_crud as crud


router = APIRouter(prefix="/authors", tags=["Authors"])

@router.get("", response_model=list[AuthorOut])
def get_authors(author: str = ""):
    return crud.get_authors(author)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=AuthorOut)
def create_new_author(auth_in: AuthorBase):
    return crud.create_new_author(auth_in)

@router.get("/{author_id}", response_model=AuthorOut)
def get_author_by_id(auth_id: int): 
    return crud.get_author_by_id(auth_id)

