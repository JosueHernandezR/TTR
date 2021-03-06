from typing import TYPE_CHECKING

from app.db.base_class import Base
from sqlalchemy import Float, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey

if TYPE_CHECKING:
    from .user import User # noqa: F401

class Prediction_Manual(Base):
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE"))
    title = Column(Text, nullable=False)
    porcentaje_aceptacion_inicial = Column(Float, nullable=False)
    tamanio_grupo_votantes = Column(Integer, nullable=False)
    jerarquias_electorales = Column(Integer, nullable=False)
    porcentaje_victoria = Column(Float, nullable=False)
    porcentaje_derrota = Column(Float, nullable=False)
    porcentaje_aceptacion_final = Column(Float, nullable=False)
    iteraciones_para_eliminación = Column(Integer, nullable=False)

    owner = relationship("User", backref="prediction_manual")