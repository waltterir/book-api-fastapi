from sqlmodel import SQLModel, Field, Relationship
from typing import List

class BookBase(SQLModel):
    book_id: int
    author: str
    title: str


class AuthorBase(SQLModel):
    name: str

class Book(BookBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    author_id: int = Field(foreign_key="author.id")
    author: "Author" = Relationship(back_populates="books")

class Author(AuthorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    books: List["Book"] = Relationship(back_populates="author")   


class BookOut(BookBase):
    id: int 
    
class AuthorOut(AuthorBase):
    id: int 
