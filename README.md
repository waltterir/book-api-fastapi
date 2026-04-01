# Book API (FastAPI)

A REST API for managing books and authors, built using FastAPI, SQLModel, and SQLite.

## Status

In progress — core backend features implemented, currently implementing JWT-based authentication and user-specific functionality

## Overview

Production-style REST API built with FastAPI, featuring authentication, testing, and cloud deployment.

- JWT authentication & protected routes
- Modular backend architecture
- Automated testing with pytest
- Deployed on GCP Ubuntu VM (Gunicorn + Uvicorn)

Designed to simulate a real-world backend system

## Core Features

- Implemented full CRUD operations for books and authors via REST API
- Relational data modeling (Author → Books)
- Endpoint for retrieving an author's books
- Offset-based pagination (page & limit)
- Search and filtering for authors by name and genre
- Search and filtering for books by title, author_id, genre, and release_year

## Authentication

- JWT-based authentication (access tokens)
- Password hashing with bcrypt (passlib)
- Login & registration flow
- Protected routes using FastAPI dependencies
- Token validation via get_current_user
- User authentication with password hashing and JWT access tokens (login flow implemented)

## Backend & Architecture

- Modular project structure (routes, database, models)
- SQLite database integration with SQLModel
- Basic error handling with HTTP exceptions
- Validation to prevent deleting authors with existing books
- Wrote comprehensive API tests with pytest (covering CRUD operations, validation, and error cases)
- Dependency-based authentication flow using FastAPI Depends
- Separation of concerns between authentication, routes, and database layers

## ⚙️ Setup & Run

### 1. Clone repository

git clone ...
cd ...

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run application

uvicorn app.main:app --reload

### 4. Open API docs

http://localhost:8000/docs

## API Usage

Interactive API documentation:

👉 Live: http://34.88.27.49:8000/docs (when server is running)
👉 Local: http://localhost:8000/docs

Includes:

- Books CRUD
- Authors CRUD
- Authentication endpoints

## Deployment

The API has been deployed to a cloud environment using Google Cloud Platform.

- Deployed the application to an Ubuntu-based VM on GCP
- Configured networking and firewall rules to expose a public API endpoint
- Configured production-ready server using Gunicorn with Uvicorn workers
- Verified the API through a public endpoint and Swagger UI

## Testing

This project includes automated tests written with pytest.

Test coverage includes:

- CRUD operations for authors and books
- Pagination and query parameter validation
- Error handling validation (covering 404, 400, 422 cases)
- Business logic validation (e.g. preventing deletion of authors with existing books)

Run tests locally:

```bash
python -m pytest -v
```

## Project Structure

app/
├── main.py
├── routes/ # API endpoints
├── models/ # SQLModel models
├── crud/ # Database operations
├── database/ # DB setup and session
├── security/ # Authentication & JWT logic
tests/ # Automated tests

## Tech Stack

- Python
- FastAPI
- SQLModel
- SQLite
- Gunicorn (application server)
- Google Cloud (Compute Engine VM)

## Project Direction

This project started as a learning exercise, but as I got deeper into backend development, I expanded it into a production-style API with authentication, testing, and cloud deployment.

## Planned Features

The following features are planned for future development:

- Role-based authorization (user vs admin)
- User-specific reading list (read / to-read / reading)
- Favorite authors functionality
- Structured error handling with meaningful HTTP responses
