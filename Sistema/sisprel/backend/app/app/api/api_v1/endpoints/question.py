from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.Question)
def create_question(
        *,
        db: Session = Depends(deps.get_db),
        question_in: schemas.QuestionCreate,
        current_user: models.User = Depends(deps.get_current_active_user),
        survey_id: int,
    ) -> Any:
    question = crud.question.create_question(db=db, question=question_in, survey_id=survey_id)
    return question

@router.get("/{id}", response_model=schemas.Question)
def read_question(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: models.User = Depends(deps.get_current_active_user),
    ) -> Any:
    """
    Get question by ID.
    """
    question = crud.question.get(db=db, id=id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    # Desarrollar la funcion de obtener encuesta con el id
    return question

@router.put("/{id}", response_model=schemas.Question)
def update_question(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        question_in: schemas.QuestionUpdate,
        current_user: models.User = Depends(deps.get_current_active_user),
    ) -> Any:
    """
    Update a question.
    """
    question = crud.question.get(db=db, id=id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    # Desarrollar la funcion de obtener encuesta con el id
    question = crud.question.update(db=db, db_obj=question, obj_in=question_in)
    return question

@router.delete("/{id}", response_model=schemas.Question)
def delete_question(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: models.User = Depends(deps.get_current_active_user),
    ) -> Any:
    """
    Delete a question.
    """
    question = crud.question.get(db=db, id=id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    # Desarrollar la funcion de obtener encuesta con el id
    question = crud.question.remove(db=db, id=id)
    return question