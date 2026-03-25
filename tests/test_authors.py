def test_authors_get(client):
    response = client.get("/authors")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_authors_with_pagination(client):
    response = client.get("/authors?page=1&limit=5")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_invalid_page(client):
    response = client.get("/authors?page=0&limit=5")
    assert response.status_code == 400

def test_create_author(client):
    payload = {
            "name": "Testi"
        }
    
    response = client.post("/authors", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Testi"
    assert "id" in data

def test_author_by_id(client):
    create_response = client.post(
        "/authors",
        json={
            "name": "Testi",
        }
    )
    author_id = create_response.json()["id"]
    response = client.get(f"/authors/{author_id}")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == author_id
    assert data["name"] == "Testi"

def test_delete_author(client):
    create_response = client.post(
        "/authors",
        json={
            "name": "Testi"
            }
        )
    author_id = create_response.json()["id"]

    response = client.delete(f"/authors/{author_id}")
    assert response.status_code == 204

def test_delete_author_not_found(client):
    response = client.delete("/authors/9999")
    assert response.status_code == 404

def test_delete_author_with_books_fails(client):
    author_response = client.post(
        "/authors", 
        json={
            "name": "Testi"
            }
        )
    author_id = author_response.json()["id"]

    client.post(
        "/books",
        json={
            "title": "The Hobbit",
            "author_id": author_id
        }
    )

    response = client.delete(f"/authors/{author_id}")
    assert response.status_code == 400
    assert response.json()["detail"] == "Cannot delete author with existing books."


def test_author_not_found(client):
    response = client.get("/authors/99999")
    assert response.status_code == 404
    assert "detail" in response.json()

def test_create_author_fails_without_name(client):
    response = client.post(
        "/authors",
        json={
            "age": 29
            }
        )
    
    assert response.status_code == 422


