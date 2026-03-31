from fastapi import APIRouter

from app.schemas.device import DeviceDetail, DeviceSummary
from app.services.devices_service import get_device, list_devices


router = APIRouter(prefix="/devices", tags=["devices"])


@router.get("", response_model=list[DeviceSummary])
async def read_devices() -> list[DeviceSummary]:
    return list_devices()


@router.get("/{device_id}", response_model=DeviceDetail)
async def read_device(device_id: str) -> DeviceDetail:
    return get_device(device_id)
