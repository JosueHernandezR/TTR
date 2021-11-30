from typing import Optional, Union, List, Dict, Any
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.predictions import Prediction_Manual
from app.schemas.prediction import PredictionCreate, PredictionUpdate
from sqlalchemy.orm import Session

class CRUDPredictionManual(CRUDBase[Prediction_Manual, PredictionCreate, PredictionUpdate]):
    def createPredictionManual(
        self, db: Session, *, obj_in: PredictionCreate, owner_id: int
    ) -> Prediction_Manual:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id = owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
prediction_manual = CRUDPredictionManual(Prediction_Manual)