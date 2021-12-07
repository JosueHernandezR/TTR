from typing import Optional, Union, List, Dict, Any
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.survey_aceptacion import Survey_Aceptacion
from app.schemas.survey_aceptacion import SurveyAceptacionCreate, SurveyAceptacionUpdate
from sqlalchemy.orm import Session

class CRUDSurveyAceptacion(CRUDBase[Survey_Aceptacion, SurveyAceptacionCreate, SurveyAceptacionUpdate]):
    def createSurveyAceptacion(
        self,
        db: Session, 
        *,
        obj_in: SurveyAceptacionCreate,
        survey_id: int,
        respondent_id: int,
        sum_weight_answers: int,
        survey_weigth_max: int
    ) -> Survey_Aceptacion:
        if(sum_weight_answers/survey_weigth_max) > 0.50:
            aceptacion = 1
        else:
            aceptacion = 0
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, survey_id = survey_id, respondent_id = respondent_id, aceptacion = aceptacion)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def get_all_aceptacion_by_survey(
        self,
        db: Session,
        *,
        survey_id: int,
    ) -> List[Survey_Aceptacion]:
        return(
            db.query(self.model)
            .filter(Survey_Aceptacion.survey_id == survey_id, Survey_Aceptacion.aceptacion == 1)
            .all()
        )
    def get_all_participants_by_survey(
        self,
        db: Session,
        *,
        survey_id: int,
    ) -> List[Survey_Aceptacion]:
        return(
            db.query(self.model)
            .filter(Survey_Aceptacion.survey_id == survey_id)
            .all()
        )

survey_aceptacion = CRUDSurveyAceptacion(Survey_Aceptacion)