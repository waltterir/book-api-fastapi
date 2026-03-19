from sqlmodel import SQLModel, create_engine, Field

class BookBase(SQLModel):
    author: str
    name: str

class Book(BookBase, table=True):
     id: int = Field(default=None, primary_key=True)

class BookIn(BookBase):
    pass

class BookOut(BookBase):
    id: int 

class AuthorBase(SQLModel):
    name: str

class Author(AuthorBase, table=True):
     id: int = Field(default=None, primary_key=True)

class AuthorOut(AuthorBase):
    id: int 
