from fastapi import APIRouter

from app.schemas.engine import EngineStatus
from app.services.engine_service import get_engine_status

router = APIRouter(prefix="/engine", tags=["engine"])


@router.get("/status", response_model=EngineStatus)
async def read_engine_status() -> EngineStatus:
    return get_engine_status()
