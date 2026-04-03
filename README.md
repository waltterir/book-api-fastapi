# Book API (FastAPI)

A REST API for managing books and authors, built using FastAPI, SQLModel, and SQLite.

## Status

Core backend features implemented, including JWT-based authentication and user-specific functionality.

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

### Run locally

Clone repository

```bash
git clone ...
cd ...
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run application

```bash
uvicorn app.main:app --reload
```

Open API docs

http://localhost:8000/docs

---

### Run with Docker

The application can be run in an isolated container using Docker.

Build the Docker image

```bash
docker build -t book-api .
```

Run the container

```bash
docker run -p 8000:8000 book-api
```

Open API docs

http://localhost:8000/docs

## API Usage

Interactive API documentation:

- Live: http://34.88.27.49:8000/docs (when server is running)
- Local: http://localhost:8000/docs

The live API is hosted on a cloud VM and may not always be running.

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

## 📁 Project Structure

```text
app/
├── main.py
├── routes/        # API endpoints
├── models/        # Database models
├── crud/          # Database operations
├── database/      # DB setup
└── security/      # Auth & JWT logic

tests/             # Automated tests
```

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

- Containerize the application with Docker
- Role-based authorization (user vs admin)
- User-specific data (reading lists / favorites)
- Favorite authors functional
