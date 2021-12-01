from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.Survey)
def create_survey(
        *, 
        db: Session = Depends(deps.get_db), 
        survey_in: schemas.SurveyCreate, 
        current_user: models.User = Depends(deps.get_current_active_user)
    ) -> Any:
    survey = crud.survey.create_user_survey(db=db, obj_in = survey_in, user_id=current_user.id)
    return survey

@router.get("/all", response_model=List[schemas.Survey])
def read_all_surveys(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        current_user: models.User = Depends(deps.get_current_active_user)
    ) -> Any:
    """
    Retrieve surveys.
    """
    surveys = crud.survey.get_multi(db, skip=skip, limit=limit)
    return surveys

@router.get("/", response_model=List[schemas.Survey])
def read_surveys_by_owner(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        current_user: models.User = Depends(deps.get_current_active_user)
    ) -> Any:
    surveys = crud.survey.get_multi_by_owner(db=db, owner_id=current_user.id, skip=skip, limit=limit)
    return surveys

@router.put("/{id}", response_model=schemas.Survey)
def update_survey(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        survey_in: schemas.SurveyUpdate,
        current_user: models.User = Depends(deps.get_current_active_user),
    ) -> Any:
    """
    Update an survey.
    """
    survey = crud.survey.get(db=db, id=id)
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    if (survey.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    survey = crud.survey.update(db=db, db_obj=survey, obj_in=survey_in)
    return survey

@router.get("/{id}", response_model=schemas.Survey)
def read_survey(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: models.User = Depends(deps.get_current_active_user),
    ) -> Any:
    """
    Get survey by ID.
    """
    survey = crud.survey.get(db=db, id=id)
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    if (survey.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return survey

@router.delete("/{id}", response_model=schemas.Survey)
def delete_survey(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: models.User = Depends(deps.get_current_active_user),
    ) -> Any:
    """
    Delete an survey.
    """
    survey = crud.survey.get(db=db, id=id)
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    if (survey.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    survey = crud.survey.remove(db=db, id=id)
    return survey

# @router.post("/{id}/addQuestion", response_model=schemas.Question)
# def create_question(
#         *,
#         db: Session = Depends(deps.get_db),
#         question_in: schemas.QuestionCreate,
#         id: int,
#         current_user: models.User = Depends(deps.get_current_active_user)
#     )-> Any:
#     question = crud.question.create_question(db=db, question = question_in, survey_id=id)
#     return question

# @router.post("/{survey_id}/{question_id}/addOption", response_model=schemas.QuestionOption)
# def create_question_option(
#         *,
#         db: Session = Depends(deps.get_db),
#         question_option_in: schemas.QuestionOptionCreate,
#         question_id: int
#     ) -> Any:
#     question_option = crud.question_option.create_question_option(db=db, question_option=question_option_in, question_id=question_id )
#     return question_option