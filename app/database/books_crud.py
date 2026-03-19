from fastapi import HTTPException, Response , status
from .models import BookIn, BookOut

books = [
    {"id": 0, "name": "Pimeä Kuu", "author": "Sofi Oksanen"},
    {"id": 1, "name": "Pahat Pojat", "author": "Vares"},
    {"id": 2, "name": "Game of Thrones", "author": "RR Martin"},
]


def get_all_books(author: str | None = None):
    if author: 
        return [b for b in books if b["author"] == author]
    return books

def create_new_book(book_in: BookIn):
    new_id = books[-1]["id"]+1
    book = BookOut(id=new_id, **book_in.model_dump())
    books.append(book.model_dump())
    return book


def get_book_by_id(book_id: int): 
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with {book_id} not found.")


def delete_book_by_id(book_id: int):
    for i, book in enumerate(books):
        if book["id"] == book_id:
            del books[i]
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with {book_id} not found.")
        