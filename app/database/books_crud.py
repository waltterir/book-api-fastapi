from fastapi import HTTPException, Response , status
from .models import BookBase, Book
from sqlmodel import Session, select


def get_all_books(session: Session, author: str | None = None):
   statement = select(Book)
   if author: 
       statement.where(Book.author == author)
   return session.exec(statement).all()

def create_new_book(session: Session, book_in: BookBase):
    book = Book.model_validate(book_in)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


def get_book_by_id(session: Session, book_id: int): 
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with {book_id} not found.")


def delete_book_by_id(sessiom: Session, book_id: int):
    for i, book in enumerate(books):
        if book["id"] == book_id:
            del books[i]
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with {book_id} not found.")
        