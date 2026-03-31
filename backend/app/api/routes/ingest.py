from fastapi import APIRouter

from app.schemas.ingest import (
    AIEventBatchIngest,
    DeviceBatchIngest,
    IngestResult,
    InspectionBatchIngest,
    TelemetryBatchIngest,
)
from app.services import runtime_store
from app.services.engine_service import ensure_external_mode

router = APIRouter(prefix="/ingest", tags=["ingest"])


@router.post("/devices", response_model=IngestResult)
async def ingest_devices(payload: DeviceBatchIngest) -> IngestResult:
    accepted = runtime_store.upsert_devices(payload.items)
    return ensure_external_mode("devices", accepted)


@router.post("/telemetry", response_model=IngestResult)
async def ingest_telemetry(payload: TelemetryBatchIngest) -> IngestResult:
    accepted = runtime_store.upsert_telemetry(payload.items)
    return ensure_external_mode("telemetry", accepted)


@router.post("/ai-events", response_model=IngestResult)
async def ingest_ai_events(payload: AIEventBatchIngest) -> IngestResult:
    accepted = runtime_store.append_ai_events(payload.items)
    return ensure_external_mode("ai-events", accepted)


@router.post("/inspections", response_model=IngestResult)
async def ingest_inspections(payload: InspectionBatchIngest) -> IngestResult:
    accepted = runtime_store.append_inspections(payload.items)
    return ensure_external_mode("inspections", accepted)
