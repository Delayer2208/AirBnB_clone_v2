#!/usr/bin/python3
"""
Module defining the Amenity class for managing amenities.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Amenity(BaseModel, Base):
    """
    Class representing an amenity in the application.

    Attributes:
        name (str): The name of the amenity.
    """
    __tablename__ = 'amenities'
    
    name = Column(String(128), nullable=False)
    # Define any additional relationships or properties here
