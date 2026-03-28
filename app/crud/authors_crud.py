from fastapi import HTTPException, status, Response
from sqlmodel import Session, select
from ..models.models import AuthorBase, Author, Book





def get_authors(session: Session,
                name: str | None = None, 
                search: str | None = None,
                authors_genre: str | None = None,
                page: int = 1, 
                limit: int = 10):
    statement = select(Author)
    if authors_genre is not None:
        statement = select(Author).join(Author.books).where(Book.genre == authors_genre).distinct()
    if name is not None: 
        statement = statement.where(Author.name == name)
    if search is not None:
        statement = statement.where(Author.name.ilike(f"%{search}%"))
    if page < 1: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Page must be atleast 1")
    if limit < 1: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Page must be atleast 1")
    
    statement = statement.order_by(Author.id)
    statement = statement.offset((page - 1) * limit)
    statement = statement.limit(limit)
    return session.exec(statement).all()

def create_author(session: Session, author_in: AuthorBase, status_code=status.HTTP_201_CREATED):
  author = Author.model_validate(author_in)
  if not author: 
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author not found")
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

def update_author(session: Session, author_id: int, author_update: AuthorBase):
    author = session.get(Author, author_id)
    if not author: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author not found.")
    author.name = author_update.name
    session.add(author)
    session.commit()
    session.refresh(author)
    return author


    





