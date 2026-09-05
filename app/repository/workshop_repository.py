
from sqlalchemy.orm import Session

from app.models import Workshop
import datetime


class WorkshopRepository:

    @staticmethod
    def get_all_available(
        db: Session
    ):
        return (
            db.query(Workshop)
            # .filter(
            #     Workshop.registration_deadline > datetime.utcnow()
            # )
            .all()
        )
        
    @staticmethod
    def get_by_id(
        db: Session,
        id: int
    ):
        return (
            db.query(Workshop)
            .filter(
                Workshop.workshop_id == id
            )
            .first()
        )

    @staticmethod
    def save(
        db: Session,
        workshop: Workshop
    ):
        db.add(workshop)
        return workshop