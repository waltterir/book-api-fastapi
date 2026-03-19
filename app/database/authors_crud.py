from fastapi import HTTPException, status
from sqlmodel import Session, select
from .models import AuthorBase, Author, AuthorOut



def get_authors(session: Session, author: str | None = None):
    if author == None:
        return session.exec(select(Author)).all()
    else: 
        return session.exec(select(Author).where(Author.name == author)).all()

def create_new_author(session: Session, auth_in: AuthorBase):
  auth = Author.model_validate(auth_in)
  session.add(auth)
  session.commit()
  session.refresh(auth)
  return auth

def get_author_by_id(session: Session, auth_id: int):
    auth = session.get(AuthorOut, auth_id)
    if not auth: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author with {auth_id} not found.")
    return auth

def delete_author_by_id(session: Session, auth_id: int):
    auth = session.get(AuthorOut, auth_id)
    if not auth:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author with {auth_id} not found.")
    session.delete(auth)
    session.commit()
    return auth


