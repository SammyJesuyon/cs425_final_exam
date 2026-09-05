# app/router/registration_router.py

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from app.database import get_db
from app.exceptions import (
    InvalidDateError,
    MaximumCapacityReachedError,
    WorkshopUnavailableError
)
from app.schemas import (
    RegistrationCreate,
    RegistrationResponse,
    WorkshopResponse
)
from app.service.registration_service import (
    RegistrationService
)
from app.service.workshop_service import (
    WorkshopService
)

# from typing import list

router = APIRouter(
    prefix="/registrations",
    tags=["Registrations"]
)


@router.post(
    "",
    response_model=RegistrationResponse,
    status_code=status.HTTP_201_CREATED
)
def create_registration(
    request: RegistrationCreate,
    db: Session = Depends(get_db)
):
    try:
        return (
            RegistrationService
            .create_registration(
                db,
                request
            )
        )

    except MaximumCapacityReachedError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_CONFLICT,
            detail=str(exc)
        )

    except WorkshopUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc)
        )

    except InvalidDateError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        )


@router.get(
    "",
    response_model=list[RegistrationResponse]
)
def get_registration(
    db: Session = Depends(get_db)
):
    return (
        RegistrationService
        .get_all_registration(
            db
        )
    )
