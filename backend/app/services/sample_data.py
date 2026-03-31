from app.schemas.ai_event import AIEvent
from app.schemas.device import DeviceDetail, DeviceSummary
from app.schemas.inspection import InspectionSummary
from app.schemas.telemetry import TelemetryPoint, TelemetrySeries


def sample_devices() -> list[DeviceSummary]:
    return [
        DeviceSummary(
            id="dev-jetson-01",
            name="Jetson Line 01",
            device_type="jetson",
            status="online",
            location="Assembly Cell A",
            last_seen="2026-03-31T00:00:00Z",
        ),
        DeviceSummary(
            id="dev-gateway-02",
            name="Gateway 02",
            device_type="industrial-pc",
            status="degraded",
            location="Warehouse Edge Rack",
            last_seen="2026-03-31T00:02:00Z",
        ),
    ]


def sample_device_detail(device_id: str) -> DeviceDetail:
    device_map = {
        device.id: DeviceDetail(
            **device.model_dump(),
            firmware_version="2026.03.1",
            tags=["vision", "iot", "critical-path"],
        )
        for device in sample_devices()
    }
    return device_map.get(
        device_id,
        DeviceDetail(
            id=device_id,
            name="Unknown device",
            device_type="unknown",
            status="offline",
            location="Unassigned",
            last_seen="2026-03-31T00:00:00Z",
            firmware_version="unknown",
            tags=["unregistered"],
        ),
    )


def sample_telemetry() -> list[TelemetrySeries]:
    return [
        TelemetrySeries(
            device_id="dev-jetson-01",
            points=[
                TelemetryPoint(
                    timestamp="2026-03-31T00:00:00Z",
                    metric="cpu_load",
                    value=42.5,
                    unit="percent",
                ),
                TelemetryPoint(
                    timestamp="2026-03-31T00:01:00Z",
                    metric="gpu_temp",
                    value=61.4,
                    unit="celsius",
                ),
            ],
        )
    ]


def sample_ai_events() -> list[AIEvent]:
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


def sample_inspections() -> list[InspectionSummary]:
    return [
        InspectionSummary(
            id="insp-701",
            device_id="dev-jetson-01",
            job_id="batch-2026-03-31-a",
            result="pass",
            defect_type=None,
            score=0.98,
            evidence_uri="s3://edge-ai-ops/evidence/batch-2026-03-31-a/frame-01.jpg",
            created_at="2026-03-31T00:03:00Z",
        ),
        InspectionSummary(
            id="insp-702",
            device_id="dev-gateway-02",
            job_id="batch-2026-03-31-b",
            result="fail",
            defect_type="seal_shift",
            score=0.81,
            evidence_uri="s3://edge-ai-ops/evidence/batch-2026-03-31-b/frame-03.jpg",
            created_at="2026-03-31T00:06:00Z",
        ),
    ]
