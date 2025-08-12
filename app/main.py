from fastapi import FastAPI
from .database import engine, Base
from .routers import auth, data

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Personal Data Hub - Backend (MVP)")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(data.router, prefix="/data", tags=["data"])
