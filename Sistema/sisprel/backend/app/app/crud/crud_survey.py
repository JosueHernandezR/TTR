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
    
    def update_weight_survey(
        self, db: Session, *, 
        db_obj: Survey, 
        obj_in: Union[SurveyUpdate, Dict[str, Any]], 
        weight_total: int
    ) -> Survey:
        db_obj.weight_total = weight_total
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


survey = CRUDSurvey(Survey)