from sqlmodel import SQLModel, create_engine, Field

class BookBase(SQLModel):
    author: str
    name: str

class BookIn(BookBase):
    pass

class BookOut(BookBase, table=True):
    id: int = Field(default=None, primary_key=True)

class AuthorBase(SQLModel):
    name: str


class AuthorOut(AuthorBase, table=True):
    id: int = Field(default=None, primary_key=True)
