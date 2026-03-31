from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class TelemetryPoint(Base):
    __tablename__ = "telemetry_points"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    device_id: Mapped[int] = mapped_column(ForeignKey("devices.id"), index=True)
    metric: Mapped[str] = mapped_column(String(64))
    value: Mapped[str] = mapped_column(String(64))
    recorded_at: Mapped[str] = mapped_column(String(64))
