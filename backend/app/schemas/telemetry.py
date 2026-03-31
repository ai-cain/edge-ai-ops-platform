from pydantic import BaseModel


class TelemetryPoint(BaseModel):
    timestamp: str
    metric: str
    value: float
    unit: str


class TelemetrySeries(BaseModel):
    device_id: str
    points: list[TelemetryPoint]
