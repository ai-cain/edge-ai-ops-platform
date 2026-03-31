from fastapi.testclient import TestClient

from app.core.config import get_settings
from app.main import app, create_app
from app.services.runtime_store import reset_runtime_store

client = TestClient(app)


def test_root_healthcheck() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "backend"}


def test_api_healthcheck() -> None:
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "scope": "api"}


def test_engine_status_reports_embedded_defaults() -> None:
    response = client.get("/api/v1/engine/status")

    assert response.status_code == 200
    assert response.json()["mode"] == "embedded"
    assert response.json()["ingest_enabled"] is False


def test_external_runtime_can_ingest_events(monkeypatch) -> None:
    monkeypatch.setenv("ENGINE_MODE", "external")
    monkeypatch.setenv("ENGINE_NAME", "cpp-vision-engine")
    monkeypatch.setenv("ENGINE_LANGUAGE", "cpp")
    monkeypatch.setenv("ENGINE_TRANSPORT", "http")
    get_settings.cache_clear()
    reset_runtime_store()

    external_client = TestClient(create_app())
    ingest_response = external_client.post(
        "/api/v1/ingest/ai-events",
        json={
            "items": [
                {
                    "id": "evt-ext-1",
                    "device_id": "cpp-camera-01",
                    "event_type": "detection",
                    "label": "bearing_defect",
                    "confidence": 0.97,
                    "severity": "high",
                    "created_at": "2026-03-31T01:00:00Z",
                }
            ]
        },
    )
    events_response = external_client.get("/api/v1/ai-events")
    status_response = external_client.get("/api/v1/engine/status")

    assert ingest_response.status_code == 200
    assert ingest_response.json()["accepted"] == 1
    assert events_response.status_code == 200
    assert events_response.json()[0]["label"] == "bearing_defect"
    assert status_response.json()["mode"] == "external"
    assert status_response.json()["engine_language"] == "cpp"

    reset_runtime_store()
    get_settings.cache_clear()
