from sqlmodel import SQLModel, Field, Relationship


class BookBase(SQLModel):
    author_id: int
    title: str
    release_year: int | None = None
    genre: str | None = None

class AuthorBase(SQLModel):
    name: str
    

class Author(AuthorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    books: list["Book"] = Relationship(back_populates="author")  

class Book(BookBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    author_id: int = Field(foreign_key="author.id")
    author: "Author" = Relationship(back_populates="books")
 

class BookOut(BookBase):
    id: int 
    
class AuthorOut(AuthorBase):
    id: int 

class AuthorWithBooks(SQLModel): 
    id: int 
    name: str
    books: list[BookOut]


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    password_hash: str

class UserCreate(SQLModel):
    email: str
    password: str

class UserLogin(SQLModel):
    email: str
    password: str


class UserOut(SQLModel):
    id: int
