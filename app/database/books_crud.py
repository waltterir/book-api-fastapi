from fastapi import HTTPException, Response, status
from sqlmodel import Session, select
from .models import BookBase, Book, Author



def get_all_books(session: Session, author_id: int | None = None, page: int = 1, limit: int = 5):
   statement = select(Book)
   if author_id is not None: 
       statement = statement.where(Book.author_id == author_id)
       
   statement = statement.order_by(Book.id)
   statement = statement.offset((page - 1) * limit)
   statement = statement.limit(limit)

   return session.exec(statement).all()

def create_new_book(session: Session, book_in: BookBase):
    author = session.get(Author, book_in.author_id)
    if not author: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author not found")
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

