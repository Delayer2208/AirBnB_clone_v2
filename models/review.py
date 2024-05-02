#!/usr/bin/python3
"""Module for Review class."""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """Class representing a review."""
    if models.is_type == "db":
        __tablename__ = 'reviews'

        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        text = ""
        place_id = ""
        user_id = ""

        def __init__(self, *args, **kwargs):
            """Initializes a new Review instance."""
            super().__init__(*args, **kwargs)
