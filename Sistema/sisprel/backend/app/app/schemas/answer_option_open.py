from typing import List, Dict, Any, Optional

from pydantic import BaseModel

class AnswerOptionOpenBase(BaseModel):
    answer_text: str
    weight_calculated: float

class AnswerOptionOpenCreate(AnswerOptionOpenBase):
    pass

class AnswerOptionOpenUpdate(AnswerOptionOpenBase):
    pass

class AnswerOptionOpenInDBBase(AnswerOptionOpenBase):
    respondent_id: int
    
    option_id: int
    option_question_id: int
    option_question_survey_id: int

    class Config:
        orm_mode = True

class AnswerOptionOpen(AnswerOptionOpenInDBBase):
    pass

class AnswerOptionOpenInDB(AnswerOptionOpenInDBBase):
    pass