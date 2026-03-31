from app.schemas.telemetry import TelemetryPoint, TelemetrySeries


def get_latest_telemetry() -> list[TelemetrySeries]:
    return [
        TelemetrySeries(
            device_id="dev-jetson-01",
            points=[
                TelemetryPoint(
                    timestamp="2026-03-31T00:00:00Z",
                    metric="cpu_load",
                    value=42.5,
                    unit="percent",
                ),
                TelemetryPoint(
                    timestamp="2026-03-31T00:01:00Z",
                    metric="gpu_temp",
                    value=61.4,
                    unit="celsius",
                ),
            ],
        )
    ]
