from pydantic import BaseModel

from app.schemas.ai_event import AIEvent
from app.schemas.device import DeviceSummary
from app.schemas.inspection import InspectionSummary
from app.schemas.telemetry import TelemetrySeries


class DeviceBatchIngest(BaseModel):
    items: list[DeviceSummary]


class TelemetryBatchIngest(BaseModel):
    items: list[TelemetrySeries]


class AIEventBatchIngest(BaseModel):
    items: list[AIEvent]


class InspectionBatchIngest(BaseModel):
    items: list[InspectionSummary]


class IngestResult(BaseModel):
    accepted: int
    stream: str
    mode: str
    engine_name: str
