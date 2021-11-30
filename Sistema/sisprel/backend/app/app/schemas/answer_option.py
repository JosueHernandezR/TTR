from typing import List, Dict, Any, Optional

from pydantic import BaseModel

class AnswerOptionBase(BaseModel):
    weight_selected: float

class AnswerOptionCreate(AnswerOptionBase):
    pass

class AnswerOptionUpdate(AnswerOptionBase):
    pass

class AnswerOptionInDBBase(AnswerOptionBase):
    respondent_id: int
    
    option_id: int
    option_question_id: int
    option_question_survey_id: int

    class Config:
        orm_mode = True

class AnswerOption(AnswerOptionInDBBase):
    pass

class AnswerOptionInDB(AnswerOptionInDBBase):
    pass