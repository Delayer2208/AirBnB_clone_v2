#!/usr/bin/python3
"""State Module for HBNB project."""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class for HBNB project."""
    if models.is_type == "db":
        __tablename__ = 'states'

        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")

    else:
        name = ""

        def __init__(self, *args, **kwargs):
            """Initializes a new State instance."""
            super().__init__(*args, **kwargs)

        @property
        def cities(self):
            """Getter attribute in case of filestorage"""
            city_list = []
            for city in list(models.storage.all(models.City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
