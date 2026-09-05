# app/models.py

from sqlalchemy import (
    Column,
    Date,
    Integer,
    String,
    DATETIME,
    Time,
    ForeignKey
)
from sqlalchemy.orm import relationship

from app.database import Base

class Workshop(Base):
    __tablename__ = "workshop"

    workshop_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=False
    )
    
    date = Column(
        Date,
        nullable=False
    )
    
    time = Column(
            Time,
            nullable=False
        )
    
    venue = Column(
        String,
        nullable=False
    )
    
    capacity = Column(
        Integer,
        nullable=False
    )

    registration_deadline = Column(
        DATETIME,
        nullable=False,
    )

    registration = relationship(
        "Registration",
        back_populates="workshop"
    )


class Registration(Base):
    __tablename__ = "transactions"

    registration_id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    
    workshop_id = Column(
        ForeignKey(Workshop.workshop_id),
        nullable=False,
        index=True,
    )

    student_id = Column(
        Integer,
        nullable=False
    )

    student_name = Column(
        String,
        nullable=False
    )

    student_email = Column(
        String,
        nullable=False,
    )

    registration_date = Column(
        Date,
        nullable=False
    )

    workshop = relationship(
        "Workshop",
        back_populates="registration"
    )