#!/usr/bin/python3
"""This module defines a class User"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """
    The User class represents a user in the HBNB project.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        places (relationship): Relationship between User and Place.
        reviews (relationship): Relationship between User and Review.
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship('Place', backref='user', cascade='delete')
    reviews = relationship('Review', backref='user', cascade='delete')
