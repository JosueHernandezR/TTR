from datetime import datetime
from typing import TYPE_CHECKING

from app.db.base_class import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Boolean, String, Text
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .user import User  # noqa: F401

class Survey(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index= True)
    description = Column(Text)
    create_at = Column(DateTime, default=datetime.utcnow())
    active_survey = Column(Boolean(), default=True)
    owner_id = Column(Integer, ForeignKey("user.id"))

    # Relacion 1 a muchos
    questions = relationship("Question", back_populates="surveys")

    # Relacion muchos a 1
    users = relationship("User", back_populates="surveys")
