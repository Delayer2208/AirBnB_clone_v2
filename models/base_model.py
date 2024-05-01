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
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

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
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: A string representation of the instance.
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current time when instance is changed.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance into a dictionary format.

        Returns:
            dict: A dictionary representation of the instance.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        return new_dict

    def delete(self):
        """
        Deletes the current instance from the storage.
        """
        models.storage.delete(self)
