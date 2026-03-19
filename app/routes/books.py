from fastapi import APIRouter, status
from ..database import books_crud
from ..database.books_crud import BookIn, BookOut


router = APIRouter(prefix="/books", tags=["Books"])


@router.get("", response_model=list[BookOut])
def get_all_books(author: str | None = None):
    return books_crud.get_all_books(author)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=BookOut)
def create_new_shoe(book_in: BookIn):
    return books_crud.create_new_shoe(book_in)

@router.get("/{book_id}", response_model=BookOut)
def get_book_by_id(book_id: int): 
    return books_crud.get_book_by_id(book_id)


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book_by_id(book_id: int):
    return books_crud.delete_book_by_id(book_id)
        