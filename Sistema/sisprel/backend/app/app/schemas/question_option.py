from typing import Optional, List

from pydantic import  BaseModel

class QuestionOptionBase(BaseModel):
    option_name: str
    option: str
    weight: int

class QuestionOptionCreate(QuestionOptionBase):
    option_name: str
    option: str
    weight: int

class QuestionOptionUpdate(QuestionOptionBase):
    pass

class QuestionOptionInDBBase(QuestionOptionBase):
    id: int
    question_id: int
    question_survey_id: int

    class Config: 
        orm_mode = True

class QuestionOption(QuestionOptionInDBBase):
    pass

class QuestionOptionInDB(QuestionOptionInDBBase):
    pass