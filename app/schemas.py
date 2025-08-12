from pydantic import BaseModel, EmailStr
from typing import Optional, Any
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class DataRecordCreate(BaseModel):
    metric: str
    value: float
    timestamp: Optional[datetime] = None
    meta_info: Optional[Any] = None

class DataRecordOut(BaseModel):
    id: int
    metric: str
    value: float
    timestamp: datetime
    meta_info: Optional[Any]
    class Config:
        orm_mode = True
