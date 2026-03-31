from app.core.config import get_settings
from app.schemas.telemetry import TelemetrySeries
from app.services import runtime_store, sample_data


def get_latest_telemetry() -> list[TelemetrySeries]:
    if get_settings().engine_mode == "external":
        return runtime_store.list_telemetry()
    return sample_data.sample_telemetry()
