from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.Prediction)
def createPrediction(
    *,
    db: Session = Depends(deps.get_db),
    prediction_in = schemas.PredictionCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    prediction = crud.prediction_manual.createPredictionManual(
        db=db,
        obj_in=prediction_in,
        owner_id=current_user.id,
    )
    return prediction

@router.get("/all", response_model=List[schemas.Prediction])
def read_all_predictions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    predictions = crud.prediction_manual.get_multi(
        db=db,
        skip=skip,
        limit=limit,
    )
    return predictions

@router.get("/", response_model=List[schemas.Prediction])
def read_all_predictions_by_owner(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    predictions = crud.prediction_manual.get_multi_by_owner(
        db = db,
        owner_id=current_user.id,
        skip=skip,
        limit=limit
    )
    return predictions