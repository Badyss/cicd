from main import app


def test_hello():
    client = app.test_client()
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json["message"] == "Hello, world!"


def test_user():
    client = app.test_client()
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json == {"badyss": "yoyoyo"}
