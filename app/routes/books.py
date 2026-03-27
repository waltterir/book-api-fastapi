from fastapi import APIRouter, status, Depends
from ..models.models import BookBase, BookOut
from ..crud import  books_crud as crud
from sqlmodel import Session
from ..database.database import get_session


router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[BookOut])
def get_all_books(*, 
                session: Session = Depends(get_session), 
                author_id: int | None = None, 
                search: str | None = None,
                genre: str | None = None,
                release_year: int | None = None,
                title: str | None = None,
                page: int = 1, 
                limit: int = 10):
    return crud.get_all_books(session, author_id, search, genre, release_year, title, page, limit)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BookOut)
def create_new_book(*, session: Session = Depends(get_session), book_in: BookBase):
    return crud.create_new_book(session, book_in)

@router.get("/{book_id}", response_model=BookOut)
def get_book_by_id(*, session: Session = Depends(get_session), book_id: int): 
    return crud.get_book_by_id(session, book_id)


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book_by_id(*, session: Session = Depends(get_session), book_id: int):
    return crud.delete_book_by_id(session, book_id)

@router.put("/{book_id}", response_model=BookOut)
def update_book_by_id(*, session: Session = Depends(get_session), book_id: int, book_update: BookBase):
    return crud.update_book_by_id(session, book_id, book_update)