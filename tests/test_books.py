def test_books_get(client):
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_book_not_found(client):
    response = client.get("/books/999999")
    assert response.status_code == 404
    assert "detail" in response.json()

def test_create_book(client):
    author_response = client.post(
        "/authors",
        json={
            "name": "Testi Author"
        }
    )
    author_id = author_response.json()["id"]

    payload = {
        "author_id": author_id,
        "title": "Testi Title",
        "release_year": 2000,
        "genre": "Testi genre",
    }

    response = client.post("/books", json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data["author_id"] == author_id
    assert "id" in data

def test_book_by_id(client):
    author_response = client.post(
        "/authors",
        json={
            "name": "Testi Author"
        }
    )
    author_id = author_response.json()["id"]

    payload = {
        "author_id": author_id,
        "title": "Testi Title",
        "release_year": 2000,
        "genre": "Testi genre",
    }

    response = client.post("/books", json=payload)
    book_id = response.json()["id"]

    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == book_id
    assert data["title"] == "Testi Title"
    assert data["author_id"] == author_id
    assert data["release_year"] == 2000
    assert data["genre"] == "Testi genre"
    
    
    
def test_delete_book(client):
    author_response = client.post(
        "/authors",
        json={
            "name": "Testi"
            }
        )
    author_id = author_response.json()["id"]

    payload = {
        "author_id": author_id,
        "title": "Testi Title",
        "release_year": 2000,
        "genre": "Testi genre",
    }

    response = client.post("/books", json=payload)
    book_id = response.json()["id"]

    response = client.delete(f"/books/{book_id}")
    assert response.status_code == 204


def test_delete_book_not_found(client):
    response = client.delete("/book/9999")
    assert response.status_code == 404

def test_create_book_with_invalid_author(client):
    payload = {
        "author_id": 9999,
        "title": "Testi Title",
        "release_year": 2000,
        "genre": "Testi genre",
    }

    response = client.post("/books", json=payload)
    assert response.status_code == 404



    