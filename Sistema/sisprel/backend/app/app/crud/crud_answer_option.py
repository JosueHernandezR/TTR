from typing import Optional, Union, List, Dict, Any
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session

from app.crud.base import CRUDBase
from app.models.answer_option import Answer_Option
from app.schemas.answer_option import AnswerOptionCreate, AnswerOptionUpdate

class CRUDAnswerOption(
        CRUDBase[
            Answer_Option,
            AnswerOptionCreate,
            AnswerOptionUpdate,
        ]
    ):
    def createAnswerOption(
        self,
        db: Session,
        *,
        obj_in: AnswerOptionCreate,
        respondent_id: int, 
        option_id: int,
        option_question_id: int,
        option_question_survey_id: int,
    ) -> Answer_Option:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            **obj_in_data,
            respondent_id = respondent_id,
            option_id = option_id,
            option_question_id = option_question_id,
            option_question_survey_id = option_question_survey_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def get_multi_by_survey(
        self, db: Session, *, option_question_survey_id: int,
        skip: int = 0, limit: int = 100,
    ) -> List[Answer_Option]:
        return(
            db.query(self.model)
            .filter(option_question_survey_id == option_question_survey_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_multi_by_survey_and_respondent(
        self, db: Session, *, option_question_survey_id:int,
        respondent_id: int, skip: int = 0, limit: int =100
    ) -> List[Answer_Option]:
        return(
            db.query(self.model)
            .filter(option_question_survey_id == option_question_survey_id and respondent_id == respondent_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
    
answer_option = CRUDAnswerOption(Answer_Option)