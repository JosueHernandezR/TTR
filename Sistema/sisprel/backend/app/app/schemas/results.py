from typing import List, Dict, Any, Optional

from pydantic import BaseModel

class ResultPredictionBase(BaseModel):
    title: str
    porcentaje_aceptacion_inicial: float
    tamanio_grupo_votantes: int
    jerarquias_electorales: int
    porcentaje_victoria: float
    porcentaje_derrota: float
    porcentaje_aceptacion_final: float

class ResultPredictionCreate(ResultPredictionBase):
    pass

class ResultPredictionUpdate(ResultPredictionBase):
    pass

class ResultPredictionInDBBase(ResultPredictionBase):
    id: int
    survey_id: int

    class Config:
        orm_mode = True

class ResultPrediction(ResultPredictionInDBBase):
    pass

class ResultPredictionInDB(ResultPredictionInDBBase):
    pass