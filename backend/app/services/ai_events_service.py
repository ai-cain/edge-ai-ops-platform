from app.schemas.ai_event import AIEvent


def list_ai_events() -> list[AIEvent]:
    return [
        AIEvent(
            id="evt-1001",
            device_id="dev-jetson-01",
            event_type="anomaly",
            label="surface_defect",
            confidence=0.93,
            severity="high",
            created_at="2026-03-31T00:04:00Z",
        ),
        AIEvent(
            id="evt-1002",
            device_id="dev-gateway-02",
            event_type="count",
            label="package_count",
            confidence=0.88,
            severity="info",
            created_at="2026-03-31T00:05:00Z",
        ),
    ]
