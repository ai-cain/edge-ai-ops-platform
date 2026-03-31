from app.core.config import get_settings
from app.schemas.inspection import InspectionSummary
from app.services import runtime_store, sample_data


def list_inspections() -> list[InspectionSummary]:
    if get_settings().engine_mode == "external":
        return runtime_store.list_inspections()
    return sample_data.sample_inspections()
