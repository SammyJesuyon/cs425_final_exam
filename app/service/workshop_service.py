# app/service/item_service.py

from sqlalchemy.orm import Session

from app.models import Workshop
from app.repository.workshop_repository import (
    WorkshopRepository
)
from app.schemas import WorkshopCreate


class WorkshopService:

    @staticmethod
    def create_workshop(
        db: Session,
        request: WorkshopCreate
    ):
        workshop = Workshop(
            title=request.title,
            description=request.description,
            date=request.workshop_date,
            time=request.workshop_time,
            venue=request.venue,
            capacity=request.capacity,
            registration_deadline=request.registration_deadline
        )

        WorkshopRepository.save(
            db,
            workshop
        )

        db.commit()
        db.refresh(workshop)

        return workshop

    @staticmethod
    def get_available_workshop(
        db: Session
    ):
        return WorkshopRepository.get_all_available(
            db
        )