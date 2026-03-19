from pydantic import BaseModel

class BookBase(BaseModel):
    author: str
    name: str

class BookIn(BookBase):
    pass

class BookOut(BookBase):
    id: int

class AuthorBase(BaseModel):
    name: str

class AuthorOut(AuthorBase):
    id: int
