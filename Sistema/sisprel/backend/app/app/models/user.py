from typing import TYPE_CHECKING
from datetime import datetime


from sqlalchemy import Boolean, Column, Integer, String,CHAR, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .survey import Survey  # noqa: F401
    from .answer import Answer  # noqa: F401


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), index=True)
    last_name = Column(String(255), index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    gender = Column(String(1))
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(
        DateTime,
        default=datetime.utcnow(),
        onupdate=datetime.utcnow(),
    )
    surveys = relationship("Survey", back_populates="users")
    answers = relationship("Answer", back_populates="users")
