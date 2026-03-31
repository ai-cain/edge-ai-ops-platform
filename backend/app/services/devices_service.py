from app.schemas.device import DeviceDetail, DeviceSummary


def list_devices() -> list[DeviceSummary]:
    return [
        DeviceSummary(
            id="dev-jetson-01",
            name="Jetson Line 01",
            device_type="jetson",
            status="online",
            location="Assembly Cell A",
            last_seen="2026-03-31T00:00:00Z",
        ),
        DeviceSummary(
            id="dev-gateway-02",
            name="Gateway 02",
            device_type="industrial-pc",
            status="degraded",
            location="Warehouse Edge Rack",
            last_seen="2026-03-31T00:02:00Z",
        ),
    ]


def get_device(device_id: str) -> DeviceDetail:
    device_map = {
        device.id: DeviceDetail(
            **device.model_dump(),
            firmware_version="2026.03.1",
            tags=["vision", "iot", "critical-path"],
        )
        for device in list_devices()
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
