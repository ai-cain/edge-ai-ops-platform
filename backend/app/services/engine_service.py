from fastapi import HTTPException, status

from app.core.config import get_settings
from app.schemas.engine import EngineStatus
from app.schemas.ingest import IngestResult


def get_engine_status() -> EngineStatus:
    settings = get_settings()
    ingest_enabled = settings.engine_mode == "external"
    return EngineStatus(
        mode=settings.engine_mode,
        engine_name=settings.engine_name,
        engine_language=settings.engine_language,
        transport=settings.engine_transport,
        frontend_contract=(
            "Frontend clients always call the backend API and never connect "
            "directly to the engine runtime."
        ),
        ingest_enabled=ingest_enabled,
        notes=(
            "Embedded mode runs the engine inside the backend process."
            if settings.engine_mode == "embedded"
            else (
                "External mode expects a Python, C++, or other runtime to "
                "push data into backend ingest endpoints."
            )
        ),
    )


def ensure_external_mode(stream: str, accepted: int) -> IngestResult:
    settings = get_settings()
    if settings.engine_mode != "external":
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Ingest endpoints are disabled while ENGINE_MODE=embedded. "
                "Switch to ENGINE_MODE=external for engines running outside the backend."
            ),
        )

    return IngestResult(
        accepted=accepted,
        stream=stream,
        mode=settings.engine_mode,
        engine_name=settings.engine_name,
    )
