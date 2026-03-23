from sqlmodel import SQLModel, Field, Relationship
from typing import List

class BookBase(SQLModel):
    author: str
    title: str

class Book(BookBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    authors: List["Author"] = Relationship(back_populates="book")

class BookOut(BookBase):
    id: int 

class AuthorBase(SQLModel):
    book_id: int
    name: str

class Author(AuthorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    book_id: int = Field(foreign_key="book.id")
    book: "Book" = Relationship(back_populates="authors")

class AuthorOut(AuthorBase):
    id: int 
