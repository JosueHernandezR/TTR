from typing import Optional, Union, List, Dict, Any

from fastapi.encoders import jsonable_encoder
from app import schemas

from app.crud.base import CRUDBase
from app.models.question_option import Question_option
from app.schemas.question_option import QuestionOptionCreate, QuestionOptionUpdate
from sqlalchemy.orm import Session

class CRUDQuestionOption(CRUDBase[Question_option, QuestionOptionCreate, QuestionOptionUpdate]):
    def get_by_question_option_id(self, db: Session, *, id:int) -> Optional[Question_option]:
        return db.query(self.model).filter(Question_option.id == id).first()

    def create_question_option(self, db: Session, *, question_option: QuestionOptionCreate, question_id: int, question_survey_id: int) -> Question_option:
        obj_in_data = jsonable_encoder(question_option)
        db_obj = self.model(**obj_in_data, question_id=question_id, question_survey_id=question_survey_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update_question_option(self, db: Session, *, db_obj: Question_option, obj_in: Union[QuestionOptionUpdate, Dict[str, Any]]) -> Question_option:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

question_option = CRUDQuestionOption(Question_option)