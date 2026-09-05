# app/main.py

from fastapi import FastAPI

from app.database import Base, engine
from app.router.registration_router import router as registration_router
from app.router.workshop_router import router as workshop_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Exam Boilerplate"
)

app.include_router(registration_router)
app.include_router(workshop_router)


@app.get("/")
def root():
    return {
        "message": "Application is running."
    }