from typing import TYPE_CHECKING
from datetime import datetime


from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .survey import Survey  # noqa: F401
    from .answer_option import Answer_Option # noqa: F401
    from .answer_option_open import Answer_Option_Open # noqa: F401

class User(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
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
    predictions_manual = relationship("Prediction_Manual", back_populates="owners")

    # Many to Many
    answer_options = relationship("Answer_Option", back_populates="respondents")
    answer_options_Open = relationship("Answer_Option_Open", back_populates="respondents")
