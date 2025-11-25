def test_create_contact_success(client):
    """Test POST /api/v1/contact with valid data"""
    data = {
        "name": "John Doe",
        "email": "john@example.com",
        "message": "This is a test message",
    }
    response = client.post("/api/v1/contact", json=data)
    assert response.status_code == 201
    result = response.json()
    assert result["name"] == data["name"]
    assert result["email"] == data["email"]
    assert result["message"] == data["message"]
    assert "id" in result
    assert "created_at" in result


def test_get_contact_success(client):
    """Test GET /api/v1/contact/{id} returns created contact"""
    # First create a contact
    data = {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "message": "Another test message",
    }
    create_response = client.post("/api/v1/contact", json=data)
    assert create_response.status_code == 201
    contact_id = create_response.json()["id"]

    # Then retrieve it
    get_response = client.get(f"/api/v1/contact/{contact_id}")
    assert get_response.status_code == 200
    result = get_response.json()
    assert result["id"] == contact_id
    assert result["name"] == data["name"]
    assert result["email"] == data["email"]
    assert result["message"] == data["message"]


def test_get_contact_not_found(client):
    """Test GET /api/v1/contact/{id} returns 404 for non-existent contact"""
    response = client.get("/api/v1/contact/99999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()


def test_create_contact_empty_name(client):
    """Test POST /api/v1/contact rejects empty name"""
    data = {
        "name": "",
        "email": "test@example.com",
        "message": "Test message",
    }
    response = client.post("/api/v1/contact", json=data)
    assert response.status_code == 422


def test_create_contact_empty_message(client):
    """Test POST /api/v1/contact rejects empty message"""
    data = {
        "name": "Test User",
        "email": "test@example.com",
        "message": "",
    }
    response = client.post("/api/v1/contact", json=data)
    assert response.status_code == 422


def test_create_contact_invalid_email(client):
    """Test POST /api/v1/contact rejects invalid email"""
    data = {
        "name": "Test User",
        "email": "not-an-email",
        "message": "Test message",
    }
    response = client.post("/api/v1/contact", json=data)
    assert response.status_code == 422

