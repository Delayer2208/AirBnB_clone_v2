#!/usr/bin/python3
"""City Module for the HBNB project."""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """The City class represents a city in the HBNB project.

    Attributes:
        name (str): The name of the city.
        state_id (str): The ID of the state to which the city belongs.
        places (relationship): Relationship to the Place class.
    """
    if models.is_type == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities', cascade='delete')
    else:
        state_id = ""
        name = ""
