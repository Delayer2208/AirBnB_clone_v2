#!/usr/bin/python3
"""Module for Amenity class."""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Amenity(BaseModel, Base):
    """Class representing an Amenity."""
    __tablename__ = 'amenities'
    
    name = Column(String(128), nullable=False)
