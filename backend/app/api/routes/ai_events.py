from fastapi import APIRouter

from app.schemas.ai_event import AIEvent
from app.services.ai_events_service import list_ai_events


router = APIRouter(prefix="/ai-events", tags=["ai-events"])


@router.get("", response_model=list[AIEvent])
async def read_ai_events() -> list[AIEvent]:
    return list_ai_events()
