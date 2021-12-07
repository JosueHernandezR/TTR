from typing import TYPE_CHECKING

from sqlalchemy import Float, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from app.db.base_class import Base

if TYPE_CHECKING:
    from .survey import Survey

class Survey_Aceptacion(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    survey_id = Column(Integer, ForeignKey("survey.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    respondent_id = Column(Integer, nullable=False)
    aceptacion = Column(Integer, nullable=False)
