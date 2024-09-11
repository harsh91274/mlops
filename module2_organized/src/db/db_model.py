"""
Database models for the machine learning project.

This module defines the database models for the machine learning project,
using SQLAlchemy ORM. The models are based on the rental apartment data.

Attributes:
None

Functions:
None

Classes:
Base: The base class for SQLAlchemy declarative base.
RentApartments: The model for rental apartments.
"""

# Import necessary libraries

from sqlalchemy import REAL, INTEGER, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import db_settings

class Base(DeclarativeBase):
    """
    The base class for SQLAlchemy declarative base.
    """
    pass  # noqa: WPS420, WPS604


class RentApartments(Base):
    """
    The model for rental apartments.

    Attributes:
    address (str): The address of the rental apartment.
    area (float): The area of the rental apartment.
    construction_year (int): The construction year of the rental apartment.
    rooms (int): The number of rooms in the rental apartment.
    bedrooms (int): The number of bedrooms in the rental apartment.
    bathrooms (int): The number of bathrooms in the rental apartment.
    balcony (str): Whether the rental apartment has a balcony or not.
    storage (str): Whether the rental apartment has storage or not.
    parking (str): Whether the rental apartment has parking or not.
    furnished (str): Whether the rental apartment is furnished or not.
    garage (str): Whether the rental apartment has a garage or not.
    garden (str): Whether the rental apartment has a garden or not.
    energy (str): The energy efficiency of the rental apartment.
    facilities (str): Additional facilities provided in the rental apartment.
    zip (str): The zip code of the rental apartment.
    neighborhood (str): The neighborhood of the rental apartment.
    rent (int): The rent of the rental apartment.

    Methods:
    None
    """
    __tablename__ = db_settings.rent_apart_table_name

    address: Mapped[str] = mapped_column(VARCHAR(), primary_key=True)
    area: Mapped[float] = mapped_column(REAL())
    constraction_year: Mapped[int] = mapped_column(INTEGER())
    rooms: Mapped[int] = mapped_column(INTEGER())
    bedrooms: Mapped[int] = mapped_column(INTEGER())
    bathrooms: Mapped[int] = mapped_column(INTEGER())
    balcony: Mapped[str] = mapped_column(VARCHAR())
    storage: Mapped[str] = mapped_column(VARCHAR())
    parking: Mapped[str] = mapped_column(VARCHAR())
    furnished: Mapped[str] = mapped_column(VARCHAR())
    garage: Mapped[str] = mapped_column(VARCHAR())
    garden: Mapped[str] = mapped_column(VARCHAR())
    energy: Mapped[str] = mapped_column(VARCHAR())
    facilities: Mapped[str] = mapped_column(VARCHAR())
    zip: Mapped[str] = mapped_column(VARCHAR())
    neighborhood: Mapped[str] = mapped_column(VARCHAR())
    rent: Mapped[int] = mapped_column(INTEGER())
