from datetime import datetime
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from app import schemas

class SurveyBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    active_survey: Optional[bool] = True
    
class SurveyCreate(SurveyBase):
    title: str

class SurveyUpdate(SurveyBase):
    pass

class SurveyInDBBase(SurveyBase):
    id: int
    title: str
    create_at: datetime
    owner_id: int
    questions: List[schemas.Question] = []
    class Config:
        orm_mode = True

class Survey(SurveyInDBBase):
    pass

class SurveyInDB(SurveyInDBBase):
    pass
