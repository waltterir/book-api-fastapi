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

## Deployment

The API has been deployed to a cloud environment using Google Cloud Platform.

- Deployed the application to an Ubuntu-based VM on GCP
- Configured networking and firewall rules to expose a public API endpoint
- Ran the application using Gunicorn with Uvicorn workers
- Verified the API through a public endpoint and Swagger UI

## Project Direction

This project started as a practice project for learning FastAPI and backend fundamentals.

The goal is to expand it into a personal reading tracker API, where users can manage their own reading lists, track reading status, and interact with books and authors.

Planned features such as authentication, authorization, and user-specific data are part of this direction.

## Endpoints

### Authors

- GET /authors
- POST /authors
- GET /authors/{id}
- PUT /authors/{author_id}
- DELETE /authors/{id}
- GET /authors/{id}/books

### Books

- GET /books
- POST /books
- GET /books/{id}
- PUT /books/{book_id}
- DELETE /books/{id}

## Planned Features

The following features are planned for future development:

- JWT-based authentication (login, token handling)
- Role-based authorization (user vs admin)
- User-specific reading list (read / to-read / reading)
- Favorite authors functionality
- Filtering and search for book and author endpoints
- Structured error handling with meaningful HTTP responses

## Tech Stack

- Python
- FastAPI
- SQLModel
- SQLite
- Gunicorn (application server)

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
```
````

## Run locally

```md
Option 1 (recommended):
uvicorn app.main:app --reload

Option 2 (FastAPI CLI):
fastapi dev app/main.py
```
