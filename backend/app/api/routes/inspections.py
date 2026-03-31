from fastapi import APIRouter

from app.schemas.inspection import InspectionSummary
from app.services.inspections_service import list_inspections

router = APIRouter(prefix="/inspections", tags=["inspections"])


@router.get("", response_model=list[InspectionSummary])
async def read_inspections() -> list[InspectionSummary]:
    return list_inspections()
