from pydantic import BaseModel


class EngineStatus(BaseModel):
    mode: str
    engine_name: str
    engine_language: str
    transport: str
    frontend_contract: str
    ingest_enabled: bool
    notes: str
