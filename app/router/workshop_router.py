# app/router/workshop_router.py

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
    WorkshopCreate,
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
    prefix="/workshops",
    tags=["Workshops"]
)


@router.post(
    "",
    response_model=WorkshopResponse,
    status_code=status.HTTP_201_CREATED
)
def create_workshop(
    request: WorkshopCreate,
    db: Session = Depends(get_db)
):
    return (
        WorkshopService
        .create_workshop(
            db,
            request
        )
    )


@router.get(
    "",
    response_model=list[WorkshopResponse]
)
def get_workshop(
    db: Session = Depends(get_db)
):
    return (
        WorkshopService
        .get_available_workshop(
            db
        )
    )
