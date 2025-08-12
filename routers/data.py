from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
from .. import schemas, deps, crud

router = APIRouter()

@router.post("/records", response_model=schemas.DataRecordOut)
def create_record(payload: schemas.DataRecordCreate, db: Session = Depends(deps.get_db), current_user=Depends(deps.get_current_user)):
    return crud.create_data_record(db, current_user.id, payload)

@router.get("/records/summary")
def summary(metric: str, start: Optional[datetime] = None, end: Optional[datetime] = None, db: Session = Depends(deps.get_db), current_user=Depends(deps.get_current_user)):
    return crud.get_daily_agg(db, current_user.id, metric, start, end)
