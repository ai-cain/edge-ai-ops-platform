from fastapi import APIRouter

from app.schemas.telemetry import TelemetrySeries
from app.services.telemetry_service import get_latest_telemetry

router = APIRouter(prefix="/telemetry", tags=["telemetry"])


@router.get("/latest", response_model=list[TelemetrySeries])
async def read_latest_telemetry() -> list[TelemetrySeries]:
    return get_latest_telemetry()
