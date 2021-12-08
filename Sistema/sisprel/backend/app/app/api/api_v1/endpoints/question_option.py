from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.QuestionOption)
def create_question_option(
    *,
    db: Session = Depends(deps.get_db),
    question_option_in: schemas.QuestionOptionCreate,
    question_id: int,
    question_survey_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    question_option = crud.question_option.create_question_option(
        db=db, 
        question_option=question_option_in, 
        question_id=question_id, 
        question_survey_id=question_survey_id
    )
    return question_option

@router.get("/{id}", response_model=schemas.QuestionOption)
def read_question_option(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: models.User = Depends(deps.get_current_active_user),
    ) -> Any:
    """
    Get question option by ID.
    """
    question_option = crud.question_option.get(db=db, id=id)
    if not question_option:
        raise HTTPException(
            status_code=404, 
            detail="Opción de pregunta no encuntrada"
        )
    # Desarrollar la funcion de obtener encuesta con el id
    return question_option

@router.put("/{id}", response_model=schemas.QuestionOption)
def update_question_option(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        question_option_in: schemas.QuestionOptionUpdate,
        current_user: models.User = Depends(deps.get_current_active_user),
    ) -> Any:
    """
    Update a question option .
    """
    question_option = crud.question_option.get(db=db, id=id)
    if not question_option:
        raise HTTPException(status_code=404, detail="Question option not found")
    # Desarrollar la funcion de obtener encuesta con el id
    question_option = crud.question_option.update(db=db, db_obj=question_option, obj_in=question_option_in)
    return question_option

@router.delete("/{id}", response_model=schemas.QuestionOption)
def update_question(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: models.User = Depends(deps.get_current_active_user),
    ) -> Any:
    """
    Delete a question option.
    """
    question_option = crud.question_option.get(db=db, id=id)
    if not question_option:
        raise HTTPException(status_code=404, detail="Question not found")
    # Desarrollar la funcion de obtener encuesta con el id
    question_option = crud.question_option.remove(db=db, id=id)
    return question_option
