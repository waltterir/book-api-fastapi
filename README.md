# Book API (FastAPI)

A REST API for managing books and authors, built using FastAPI, SQLModel, and SQLite.

## Status

In progress – core functionality implemented, further improvements planned

## Features

- Implemented full CRUD operations for books and authors via REST API
- Relational data modeling (Author → Books)
- Endpoint for retrieving an author's books
- SQLite database integration with SQLModel
- Basic error handling with HTTP exceptions
- Validation to prevent deleting authors with existing books
- Modular project structure (routes, database, models)
- Offset-based pagination (page & limit)
- Wrote comprehensive API tests with pytest (covering CRUD operations, validation, and error cases)

## Example Endpoints

- GET /authors
- POST /authors
- GET /authors/{id}
- DELETE /authors/{id}

- GET /books
- POST /books
- GET /books/{id}
- DELETE /books/{id}

- GET /authors/{id}/books

## Planned Features

The following features are planned for future development:

- JWT-based authentication with user accounts and protected routes
- Owner-based authorization (users can manage only their own books)
- Filtering and search for book and author endpoints
- Structured error handling with meaningful HTTP responses

## Tech Stack

- Python
- FastAPI
- SQLModel
- SQLite

## Testing

This project includes automated tests written with pytest.

Test coverage includes:

- CRUD operations for authors and books
- Pagination and query parameter validation
- Error handling validation (covering 404, 400, 422 cases)
- Business logic validation (e.g. preventing deletion of authors with existing books)

````md
Run tests locally:

```bash
python -m pytest -v

````

## Run locally

Option 1 (recommended):
uvicorn app.main:app --reload

Option 2 (FastAPI CLI):
fastapi dev app/main.py
