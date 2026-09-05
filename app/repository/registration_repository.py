# app/repository/item_repository.py

from sqlalchemy.orm import Session

from app.models import Registration



class RegistrationRepository:

    @staticmethod
    def get_all_available(
        db: Session
    ):
        return (
            db.query(Registration)
            .all()
        )

    @staticmethod
    def get_count_by_workshop_id(
        db: Session,
        id: int
    ):
        return (
                    db.query(Registration)
                    .filter(
                        Registration.workshop_id == id
                    )
                    .count()
                )

    @staticmethod
    def save(
        db: Session,
        registration: Registration
    ):
        db.add(registration)
        return registration