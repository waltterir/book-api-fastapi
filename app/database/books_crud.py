from fastapi import HTTPException, Response, status
from sqlmodel import Session, select
from .models import BookBase, Book



def get_all_books(session: Session, author: str | None = None):
   statement = select(Book)
   if author: 
       statement = statement.where(Book.author == author)
   return session.exec(statement).all()

def create_new_book(session: Session, book_in: BookBase):
    book = Book.model_validate(book_in)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


def get_book_by_id(session: Session, book_id: int): 
    book = session.get(Book, book_id)
    if not book: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with {book_id} not found.")
    return book


def delete_book_by_id(session: Session, book_id: int):
    book = session.get(Book, book_id)
    if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with {book_id} not found.")
    session.delete(book)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)