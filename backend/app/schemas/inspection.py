from pydantic import BaseModel


class InspectionSummary(BaseModel):
    id: str
    device_id: str
    job_id: str
    result: str
    defect_type: str | None
    score: float
    evidence_uri: str
    created_at: str
