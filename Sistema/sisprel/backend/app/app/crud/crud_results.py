from typing import Optional, Union, List, Dict, Any
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.results import Survey_Results
from app.schemas.results import ResultPredictionCreate, ResultPredictionUpdate
from sqlalchemy.orm import Session

from app.calculo_final import Calculo_final

class CRUDSurveyResults(CRUDBase[Survey_Results, ResultPredictionCreate, ResultPredictionUpdate]):
    def createSurveyResults(
        self, db: Session, *, obj_in: ResultPredictionCreate, survey_id: int, 
        num_aceptacion: int,
        num_participantes: int,
    ) -> Survey_Results:
        # Calculos
        n = 0
        p0 = 0.0
        r = 0
        ecs = Calculo_final()
        ecs.reset()
        n = obj_in.jerarquias_electorales
        p0 = num_aceptacion/num_participantes
        r = obj_in.tamanio_grupo_votantes

        ecs.calculo_final(n, p0, r)

        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            **obj_in_data, 
            survey_id = survey_id,
            porcentaje_aceptacion_inicial = p0 * 100,
            porcentaje_derrota = ecs.get_pndr(),
            porcentaje_victoria = ecs.get_pnfr(),
            porcentaje_aceptacion_final = ecs.get_pn(),
            iteraciones_para_eliminación = ecs.calcular_eliminacion_total()
        )
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