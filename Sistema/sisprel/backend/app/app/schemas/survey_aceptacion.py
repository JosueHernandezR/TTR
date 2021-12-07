from typing import List, Dict, Any, Optional

from pydantic import BaseModel

class SurveyAceptacionBase(BaseModel):
    pass

class SurveyAceptacionCreate(SurveyAceptacionBase):
    pass

class SurveyAceptacionUpdate(SurveyAceptacionBase):
    pass

class SurveyAceptacionInDBBase(SurveyAceptacionBase):
    id: int
    survey_id: int
    respondent_id: int

    aceptacion: int

    class Config:
        orm_mode = True
    
class SurveyAceptacion(SurveyAceptacionInDBBase):
    pass

class SurveyAceptacionInDB(SurveyAceptacionInDBBase):
    pass