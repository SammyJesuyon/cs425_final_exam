
from sqlalchemy.orm import Session

from app.exceptions import (
    InvalidDateError,
    WorkshopUnavailableError,
    MaximumCapacityReachedError
)

from app.models import Registration
from app.repository.workshop_repository import (
    WorkshopRepository
)
from app.repository.registration_repository import (
    RegistrationRepository
)
from app.schemas import RegistrationCreate

import datetime

from app.schemas import (
    RegistrationResponse
)


class RegistrationService:

    # @staticmethod
    # def get_registration(
    #     db: Session,
    #     transaction_id: int
    # ):
    #     transaction = (
    #         TransactionRepository.get_by_id(
    #             db,
    #             transaction_id
    #         )
    #     )

    #     if not transaction:
    #         raise TransactionNotFoundError(
    #             "Transaction not found."
    #         )

    #     return transaction
    
    @staticmethod
    def get_all_registration(
            db: Session
        ):
            return RegistrationRepository.get_all_available(
                db
            )

    @staticmethod
    def create_registration(
        db: Session,
        request: RegistrationCreate
    ):
        workshop = WorkshopRepository.get_by_id(
            db,
            request.workshop_id
        )

        if not workshop:
            raise WorkshopUnavailableError(
                f"Wokshop with ID "
                f"{request.workshop_id} "
                f"was not found."
            )

        if workshop.registration_deadline is datetime.datetime.now:
            raise InvalidDateError(
                f"Workshop with ID "
                f"{request.item_id} "
                f"has passed deadline."
            )

        if RegistrationRepository.get_count_by_workshop_id(db, request.workshop_id) == workshop.capacity:
            raise MaximumCapacityReachedError(
                "Maximum capacity reached for this event"
            )

        registration = Registration(
            student_id=request.student_id,
            student_name=request.student_name,
            student_email=request.student_email,
            registration_date=datetime.datetime.now
        )

        try:
            RegistrationRepository.save(
                db,
                registration
            )

            db.commit()
            db.refresh(registration)

            return registration

        except Exception:
            db.rollback()
            raise