from typing import Optional, Union, List, Dict, Any
from fastapi.encoders import jsonable_encoder

from app import crud, models, schemas

from app.crud.base import CRUDBase
from app.models.survey import Survey
from app.schemas.survey import SurveyCreate, SurveyUpdate
from sqlalchemy.orm import Session


class CRUDSurvey(CRUDBase[Survey, SurveyCreate, SurveyUpdate]):
    def create_user_survey(
            self, db: Session, *, obj_in: SurveyCreate, user_id: int
        ) -> Survey:

        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id = user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        # for question in obj_in.question:
        #     db_question_option = models.Question(**question, question_id=db_obj.id)
        #     db.add(db_question_option)
        #     db.commit()
        #     # if db_question_option.accept_open_answer == False:
        #     #     for question_option in 
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Survey]:
        return (
            db.query(self.model)
            .filter(Survey.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

survey = CRUDSurvey(Survey)