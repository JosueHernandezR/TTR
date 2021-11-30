from typing import Optional, Union, List, Dict, Any
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.results import Survey_Results
from app.schemas.results import ResultPredictionCreate, ResultPredictionUpdate
from sqlalchemy.orm import Session

class CRUDSurveyResults(CRUDBase[Survey_Results, ResultPredictionCreate, ResultPredictionUpdate]):
    def createSurveyResults(
        self, db: Session, *, obj_in: ResultPredictionCreate, survey_id: int
    ) -> Survey_Results:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, survey_id = survey_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def get_multi_by_survey(
        self, db: Session, *, survey_id:int, skip: int = 0, limit: int = 100
    ) -> List[Survey_Results]:
        return(
            db.query(self.model)
            .filter(Survey_Results.survey_id == survey_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

survey_result = CRUDSurveyResults(Survey_Results)