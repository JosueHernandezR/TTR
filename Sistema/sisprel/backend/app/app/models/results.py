from typing import TYPE_CHECKING

from sqlalchemy import Float, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from app.db.base_class import Base

if TYPE_CHECKING:
    from .survey import Survey

class Survey_Results(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    survey_id = Column(Integer, ForeignKey("survey.id", ondelete="CASCADE", onupdate="CASCADE"))
    title = Column(Text, nullable=False)
    porcentaje_aceptacion_inicial = Column(Float, nullable=False)
    tamanio_grupo_votantes = Column(Integer, nullable=False)
    jerarquias_electorales = Column(Integer, nullable=False)
    porcentaje_victoria = Column(Float, nullable=False)
    porcentaje_derrota = Column(Float, nullable=False)
    porcentaje_aceptacion_final = Column(Float, nullable=False)

    surveys = relationship("Survey", back_populates="results")