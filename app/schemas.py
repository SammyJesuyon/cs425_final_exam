# app/schemas.py

from datetime import date, time, datetime

from pydantic import BaseModel, ConfigDict


class WorkshopCreate(BaseModel):
    workshop_id: int
    title: str
    description: str
    workshop_date: date
    workshop_time: time
    venue: str
    capacity: int
    registration_deadline: date


class WorkshopResponse(BaseModel):
    workshop_id: int
    title: str
    description: str
    workshop_date: date
    workshop_time: time
    venue: str
    capacity: int
    registration_deadline: date

    model_config = ConfigDict(
        from_attributes=True
    )


class RegistrationCreate(BaseModel):
    workshop_id: int
    student_id: int
    student_name: str
    student_email: str
    # registration_date: datetime


class RegistrationResponse(BaseModel):
    registration_id: int
    registration_id: int
    workshop_id: int
    student_id: int
    student_name: str
    student_email: str
    registration_date: date

    model_config = ConfigDict(
        from_attributes=True
    )