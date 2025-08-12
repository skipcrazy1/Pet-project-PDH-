from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas
from datetime import datetime

def create_user(db: Session, email: str, hashed_password: str):
    u = models.User(email=email, hashed_password=hashed_password)
    db.add(u); db.commit(); db.refresh(u)
    return u

def create_data_record(db: Session, user_id: int, payload: schemas.DataRecordCreate):
    ts = payload.timestamp or datetime.utcnow()
    r = models.DataRecord(user_id=user_id, metric=payload.metric, value=payload.value, timestamp=ts, meta_info=payload.metadata)
    db.add(r); db.commit(); db.refresh(r)
    return r

def get_daily_agg(db: Session, user_id: int, metric: str, start=None, end=None):
    q = db.query(func.date_trunc('day', models.DataRecord.timestamp).label('day'),
                 func.avg(models.DataRecord.value).label('avg_value'))           .filter(models.DataRecord.user_id == user_id, models.DataRecord.metric == metric)
    if start: q = q.filter(models.DataRecord.timestamp >= start)
    if end: q = q.filter(models.DataRecord.timestamp <= end)
    q = q.group_by('day').order_by('day')
    return [{"day": row.day.isoformat(), "avg": float(row.avg_value)} for row in q.all()]
