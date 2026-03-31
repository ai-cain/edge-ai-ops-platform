from pydantic import BaseModel


class AIEvent(BaseModel):
    id: str
    device_id: str
    event_type: str
    label: str
    confidence: float
    severity: str
    created_at: str
