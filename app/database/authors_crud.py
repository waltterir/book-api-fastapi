from fastapi import HTTPException, status, Response
from sqlmodel import Session, select
from .models import AuthorBase, Author, Book 




def get_authors(session: Session, book_id: int | None = None):
    statement = select(Author)
    if book_id is not None: 
        statement = statement.where(Author.book_id == book_id)
    return session.exec(statement).all()

def create_author(session: Session, auth_in: AuthorBase):
  book = session.get(Book, auth_in.book_id)
  if not book: 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book not found")
  auth = Author.model_validate(auth_in)
  session.add(auth)
  session.commit()
  session.refresh(auth)
  return auth

def get_author_by_id(session: Session, auth_id: int):
    auth = session.get(Author, auth_id)
    if not auth: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author with {auth_id} not found.")
    return auth

def delete_author_by_id(session: Session, auth_id: int):
    auth = session.get(Author, auth_id)
    if not auth:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author with {auth_id} not found.")
    session.delete(auth)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def get_book_authors(book_id: int, session: Session):
    book = session.get(Book, book_id)
    if not book: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book not found")
    return book.authors


