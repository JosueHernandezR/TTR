from typing import Optional, List

from pydantic import  BaseModel

class QuestionOptionBase(BaseModel):
    option_name: Optional[str]
    option: Optional[str]
    weight: Optional[int]

class QuestionOptionCreate(QuestionOptionBase):
    option_name: Optional[str]
    option: Optional[str]
    weight: Optional[int]

class QuestionOptionUpdate(QuestionOptionBase):
    pass

class QuestionOptionInDBBase(QuestionOptionBase):
    id: Optional[int]
    question_id: Optional[int]
    question_survey_id: Optional[int]

    class Config: 
        orm_mode = True

class QuestionOption(QuestionOptionInDBBase):
    pass

class QuestionOptionInDB(QuestionOptionInDBBase):
    pass