from fastapi import HTTPException, status, Response
from sqlmodel import Session, select
from .models import AuthorBase, Author




def get_authors(session: Session, author: str | None = None):
    statement = select(Author)
    if author: 
        statement = statement.where(Author.name == author)
    return session.exec(statement).all()

def create_new_author(session: Session, auth_in: AuthorBase):
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


