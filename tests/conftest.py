import pytest
from fastapi.testclient import TestClient

from backend.main import app
from backend.main import get_ai_service
from backend.services.fake_ai_service import FakeAIService


@pytest.fixture
def client():

    app.dependency_overrides[get_ai_service] = (
        lambda: FakeAIService()
    )

    yield TestClient(app)

    app.dependency_overrides.clear()