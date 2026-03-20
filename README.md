# Book API (FastAPI)

A REST API for managing books and authors, built with FastAPI, SQLModel and SQLite.

## Status

In progress – actively being developed

## Features

- CRUD operations for books and authors
- SQLite database integration with SQLModel
- Basic error handling with HTTP exceptions
- Modular project structure (routes, database, models)

## Tech Stack

- FastAPI
- SQLModel
- SQLite

## Run locally

Option 1 (recommended):
uvicorn app.main:app --reload

Option 2 (FastAPI CLI):
fastapi dev app/main.py
