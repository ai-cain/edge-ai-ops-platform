from pydantic import BaseModel


class DeviceSummary(BaseModel):
    id: str
    name: str
    device_type: str
    status: str
    location: str
    last_seen: str


class DeviceDetail(DeviceSummary):
    firmware_version: str
    tags: list[str]
