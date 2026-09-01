def test_chat_endpoint(client):

    response = client.post(
        "/chat",
        json={
            "message": "Hola"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["response"] == (
        "FAKE RESPONSE: I received your message: 'Hola'"
    )


def test_health_check(client):

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "ok"
    }


def test_chat_requires_message(client):

    response = client.post(
        "/chat",
        json={}
    )

    assert response.status_code == 422


def test_chat_rejects_empty_message(client):

    response = client.post(
        "/chat",
        json={
            "message": ""
        }
    )

    assert response.status_code == 422