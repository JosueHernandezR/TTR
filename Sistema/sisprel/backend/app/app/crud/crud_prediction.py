from typing import Optional, Union, List, Dict, Any
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.predictions import Prediction_Manual
from app.schemas.prediction import PredictionCreate, PredictionUpdate
from sqlalchemy.orm import Session

from app.calculo_final import Calculo_final

class CRUDPredictionManual(CRUDBase[Prediction_Manual, PredictionCreate, PredictionUpdate]):
    def createPredictionManual(
        self, db: Session, *, obj_in: PredictionCreate, owner_id: int
    ) -> Prediction_Manual:
        ecs = Calculo_final()
        ecs.reset()
        n = 0
        p0 = 0.0
        r = 0
        n = obj_in.jerarquias_electorales
        p0 = obj_in.porcentaje_aceptacion_inicial / 100
        r = obj_in.tamanio_grupo_votantes

        ecs.calculo_final(n, p0, r)

        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            **obj_in_data, 
            owner_id = owner_id, 
            porcentaje_derrota = ecs.get_pndr(),
            porcentaje_victoria = ecs.get_pnfr(),
            porcentaje_aceptacion_final = ecs.get_pn(),
            iteraciones_para_eliminación = ecs.calcular_eliminacion_total()
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        ecs.reset()
        return db_obj
    
    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100,
    ) -> List[Prediction_Manual]:
        return(
            db.query(self.model)
            .filter(Prediction_Manual.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

prediction_manual = CRUDPredictionManual(Prediction_Manual)