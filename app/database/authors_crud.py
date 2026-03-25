from fastapi import HTTPException, status, Response
from sqlmodel import Session, select
from .models import AuthorBase, Author




def get_authors(session: Session, name: str | None = None, page: int = 1, limit: int = 5):
    statement = select(Author)
    if name is not None: 
        statement = statement.where(Author.name == name)
    if page < 1: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Page must be atleast 1")
    
    statement = statement.order_by(Author.id)
    statement = statement.offset((page - 1) * limit)
    statement = statement.limit(limit)
    return session.exec(statement).all()

def create_author(session: Session, author_in: AuthorBase):
  author = Author.model_validate(author_in)
  session.add(author)
  session.commit()
  session.refresh(author)
  return author

def get_author_by_id(session: Session, author_id: int):
    author = session.get(Author, author_id)
    if not author: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author with id {author_id} not found.")
    return author

def delete_author_by_id(session: Session, author_id: int):
    author = session.get(Author, author_id)
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author with id {author_id} not found.")
    if author.books:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cannot delete author with existing books.")
    session.delete(author)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def get_author_books(session: Session, author_id: int):
    author = session.get(Author, author_id)
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author with id {author_id} not found.")
    return author


