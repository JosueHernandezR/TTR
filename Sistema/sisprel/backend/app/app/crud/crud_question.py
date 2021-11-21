from typing import Dict, Any, Optional, Union

from fastapi.encoders import jsonable_encoder
from app import crud, models, schemas

from app.crud.base import CRUDBase
from app.models.question import Question
from app.schemas.question import QuestionCreate, QuestionUpdate
from sqlalchemy.orm import Session

class CRUDQuestion(CRUDBase[Question,QuestionCreate, QuestionUpdate]):
    def get_by_question_id(self, db: Session, *, id:int) -> Optional[Question]:
        return db.query(self.model).filter(Question.id == id).first()

    def create_question(
            self, db: Session, *, question: QuestionCreate, survey_id:int
        ) -> Question:
        obj_in_data = jsonable_encoder(question)
        db_obj = self.model(**obj_in_data, survey_id = survey_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        # for question_option in question.question_options:
        #     db_question_option = models.Question_option(**question_option, question_id=db_obj.id)
        #     db.add(db_question_option)
        #     db.commit()
        return db_obj


    # def update_survey(self, db: Session, *, db_obj: Question, obj_in: Union[QuestionUpdate, Dict[str, Any]],) -> Question:
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.dict(exclude_unset=True)

    #     return super().update(db, db_obj=db_obj, obj_in=update_data)
    
question = CRUDQuestion(Question)