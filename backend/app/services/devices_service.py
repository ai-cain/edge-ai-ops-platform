from app.core.config import get_settings
from app.schemas.device import DeviceDetail, DeviceSummary
from app.services import runtime_store, sample_data


def list_devices() -> list[DeviceSummary]:
    if get_settings().engine_mode == "external":
        return runtime_store.list_devices()
    return sample_data.sample_devices()


def get_device(device_id: str) -> DeviceDetail:
    settings = get_settings()
    if settings.engine_mode == "external":
        device_map = {
            device.id: DeviceDetail(
                **device.model_dump(),
                firmware_version="external-runtime",
                tags=["external-engine", settings.engine_language],
            )
            for device in runtime_store.list_devices()
        }
        return device_map.get(
            device_id,
            DeviceDetail(
                id=device_id,
                name="Unknown device",
                device_type="unknown",
                status="offline",
                location="Unassigned",
                last_seen="2026-03-31T00:00:00Z",
                firmware_version="unknown",
                tags=["unregistered"],
            ),
        )

    return sample_data.sample_device_detail(device_id)
