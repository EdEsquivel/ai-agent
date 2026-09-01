from fastapi.testclient import TestClient

from backend.main import app
from backend.main import get_ai_service
from backend.services.fake_ai_service import FakeAIService


client = TestClient(app)


def test_chat_endpoint():

    app.dependency_overrides[get_ai_service] = (
        lambda: FakeAIService()
    )

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

    app.dependency_overrides.clear()

def test_health_check():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "ok"
    }