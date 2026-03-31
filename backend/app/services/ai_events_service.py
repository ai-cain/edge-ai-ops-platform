from app.core.config import get_settings
from app.schemas.ai_event import AIEvent
from app.services import runtime_store, sample_data


def list_ai_events() -> list[AIEvent]:
    if get_settings().engine_mode == "external":
        return runtime_store.list_ai_events()
    return sample_data.sample_ai_events()
