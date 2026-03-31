from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Inspection(Base):
    __tablename__ = "inspections"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    device_id: Mapped[int] = mapped_column(ForeignKey("devices.id"), index=True)
    job_id: Mapped[str] = mapped_column(String(120), index=True)
    result: Mapped[str] = mapped_column(String(32))
    evidence_uri: Mapped[str] = mapped_column(String(255))
