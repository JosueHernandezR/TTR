from typing import List, Dict, Any, Optional

from pydantic import BaseModel

class PredictionBase(BaseModel):
    title: str
    porcentaje_aceptacion_inicial: float
    tamanio_grupo_votantes: int
    jerarquias_electorales: int


class PredictionCreate(PredictionBase):
    pass

class PredictionUpdate(PredictionBase):
    pass

class PredictionInDBBase(PredictionBase):
    id: int
    owner_id: int

    porcentaje_victoria: float
    porcentaje_derrota: float
    porcentaje_aceptacion_final: float
    iteraciones_para_eliminación: int

    class Config:
        orm_mode = True

class Prediction(PredictionInDBBase):
    pass

class PredictionInDB(PredictionInDBBase):
    pass
