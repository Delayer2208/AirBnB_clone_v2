#!/usr/bin/python3
"""
Module defining a base class for all models in our HBNB clone.
"""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

if models.is_type == "db":
    Base = declarative_base()
else:
    Base = object

class BaseModel:
    """
    Base class for all models in the HBNB clone application.
    
    Attributes:
        id (str): The unique identifier for the model instance.
        created_at (datetime): The datetime when the instance was created.
        updated_at (datetime): The datetime when the instance was last updated.
    """
    if models.is_type == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow())
        updated_at = Column(DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initializes a new model instance.

        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            # Handle initialization with kwargs
            pass

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: A string representation of the instance.
        """
        pass

    def save(self):
        """
        Updates the updated_at attribute with the current time when instance is changed.
        """
        pass

    def to_dict(self):
        """
        Converts the instance into a dictionary format.

        Returns:
            dict: A dictionary representation of the instance.
        """
        pass

    def delete(self):
        """
        Deletes the current instance from the storage.
        """
        pass
