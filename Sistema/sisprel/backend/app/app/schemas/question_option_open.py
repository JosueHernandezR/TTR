from typing import Optional, List

from pydantic import BaseModel

class QuestionOptionOpenBase(BaseModel):
    weight_max: int

class QuestionOptionOpenCreate(QuestionOptionOpenBase):
    weight_max: int

class QuestionOptionOpenUpdate(QuestionOptionOpenBase):
    pass

class QuestionOptionOpenInDBBase(QuestionOptionOpenBase):
    id: int
    question_id: int
    question_survey_id: int

    class Config:
        orm_mode = True

class QuestionOptionOpen(QuestionOptionOpenInDBBase):
    pass

class QuestionOptionOpenInDB(QuestionOptionOpenInDBBase):
    pass
