from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_healthcheck() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "backend"}


def test_api_healthcheck() -> None:
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "scope": "api"}
