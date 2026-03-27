from fastapi import HTTPException, Response, status
from sqlmodel import Session, select
from ..models.models import BookBase, Book, Author



def get_all_books(
                session: Session, 
                author_id: int | None = None,
                search: str | None = None,
                genre: str | None = None,
                release_year: int | None = None,
                title: str | None = None,
                page: int = 1, 
                limit: int = 10):
    statement = select(Book)
    if author_id is not None: 
       statement = statement.where(Book.author_id == author_id)
    if search is not None: 
       statement = statement.where(Book.title.ilike(f"%{search}%"))
    if genre is not None: 
       statement = statement.where(Book.genre == genre)
    if release_year is not None: 
       statement = statement.where(Book.release_year == release_year)
    if title is not None:
       statement = statement.where(Book.title == title)
    if page < 1:
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Page must be atleast 1")
    if limit < 1:
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Limit must be atleast 1")
  
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

def update_book_by_id(session: Session, book_id: int, book_update: BookBase):
    book = session.get(Book, book_id)
    if not book: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with {book_id} not found.")
    author = session.get(Author, book_update.author_id)
    if not author: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author not found.")
    book.title = book_update.title
    book.release_year = book_update.release_year
    book.genre = book_update.genre
    book.author_id = book_update.author_id
    session.add(book)
    session.commit()
    session.refresh(book)
    return book
    

