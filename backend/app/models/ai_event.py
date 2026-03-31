from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class AIEventRecord(Base):
    __tablename__ = "ai_events"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    device_id: Mapped[int] = mapped_column(ForeignKey("devices.id"), index=True)
    event_type: Mapped[str] = mapped_column(String(64))
    label: Mapped[str] = mapped_column(String(120))
    severity: Mapped[str] = mapped_column(String(32), default="info")
