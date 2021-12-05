from typing import List, Dict, Any, Optional

from pydantic import BaseModel

class PredictionBase(BaseModel):
    title: str
    porcentaje_aceptacion_inicial: Optional[float]
    tamanio_grupo_votantes: Optional[int]
    jerarquias_electorales: Optional[int]
    porcentaje_victoria: Optional[float]
    porcentaje_derrota: Optional[float]
    porcentaje_aceptacion_final: Optional[float]

class PredictionCreate(PredictionBase):
    pass

class PredictionUpdate(PredictionBase):
    pass

class PredictionInDBBase(PredictionBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class Prediction(PredictionInDBBase):
    pass

class PredictionInDB(PredictionInDBBase):
    pass
