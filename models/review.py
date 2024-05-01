#!/usr/bin/python3
"""Review module for the HBNB project"""

from models.base_model import BaseModel, Base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, String
import models

class Review(BaseModel, Base):
    """
    The Review class represents a review for a place in the HBNB project.

    Attributes:
        text (str): The text content of the review.
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who created the review.
    """
    if models.is_type == 'db':
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
