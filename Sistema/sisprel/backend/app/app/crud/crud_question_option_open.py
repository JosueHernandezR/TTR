from typing import Optional, Union, List, Dict, Any

from fastapi.encoders import jsonable_encoder
from app import schemas

from app.crud.base import CRUDBase
from app.models.question_option_open import Question_option_open
from app.schemas.question_option_open import QuestionOptionOpenCreate, QuestionOptionOpenUpdate
from sqlalchemy.orm import Session

class CRUDQuestionOptionOpen(CRUDBase[Question_option_open, QuestionOptionOpenCreate, QuestionOptionOpenUpdate]):
    def get_by_question_option_open_id(self, db: Session, *, id: int) ->Optional[Question_option_open]:
        return db.query(self.model).filter(Question_option_open.id==id).first()
    
    def create_question_option_open(
            self, db: Session, *, question_option_open: QuestionOptionOpenCreate, question_id:int, question_survey_id:int
        ) -> Question_option_open:
        obj_in_data = jsonable_encoder(question_option_open)
        db_obj = self.model(**obj_in_data, question_id = question_id, question_survey_id = question_survey_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update_question_option(self, db: Session, *, db_obj: Question_option_open, obj_in: Union[QuestionOptionOpenUpdate, Dict[str, Any]]) -> Question_option_open:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

question_option_open = CRUDQuestionOptionOpen(Question_option_open)