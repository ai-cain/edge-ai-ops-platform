from collections import OrderedDict

from app.schemas.ai_event import AIEvent
from app.schemas.device import DeviceSummary
from app.schemas.inspection import InspectionSummary
from app.schemas.telemetry import TelemetrySeries

_devices: OrderedDict[str, DeviceSummary] = OrderedDict()
_telemetry: OrderedDict[str, TelemetrySeries] = OrderedDict()
_ai_events: list[AIEvent] = []
_inspections: list[InspectionSummary] = []


def reset_runtime_store() -> None:
    _devices.clear()
    _telemetry.clear()
    _ai_events.clear()
    _inspections.clear()


def upsert_devices(items: list[DeviceSummary]) -> int:
    for item in items:
        _devices[item.id] = item
    return len(items)


def list_devices() -> list[DeviceSummary]:
    return sorted(_devices.values(), key=lambda item: item.name.lower())


def upsert_telemetry(items: list[TelemetrySeries]) -> int:
    for item in items:
        _telemetry[item.device_id] = item
    return len(items)


def list_telemetry() -> list[TelemetrySeries]:
    return list(_telemetry.values())


def append_ai_events(items: list[AIEvent]) -> int:
    _ai_events[0:0] = items
    del _ai_events[100:]
    return len(items)


def list_ai_events() -> list[AIEvent]:
    return list(_ai_events)


def append_inspections(items: list[InspectionSummary]) -> int:
    _inspections[0:0] = items
    del _inspections[100:]
    return len(items)


def list_inspections() -> list[InspectionSummary]:
    return list(_inspections)
