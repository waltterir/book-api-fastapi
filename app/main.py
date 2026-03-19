from contextlib import asynccontextmanager
from fastapi import FastAPI
from .routes import books, authors
from .database.database import create_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Startataan")
    create_db()
    yield
    print("sammutetaan")

app = FastAPI(lifespan=lifespan)
app.include_router(books.router)
app.include_router(authors.router)