"""Defines a base class for all models in our HBNB clone."""
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
    Base class for all HBNB models.

    Attributes:
        id (str): The unique identifier for the model instance.
        created_at (datetime): The date and time when the instance was created.
        updated_at (datetime): The date and time when the instance was last updated.
    """

    if models.is_type == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow())
        updated_at = Column(DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initializes a new model instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())
            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = datetime.now()
            else:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.now()
            else:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if '__class__' in kwargs:
                del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: A string representation of the instance.
        """
        cls_name = str(type(self)).split('.')[-1].split('\'')[0]
        return '[{}] ({}) {}'.format(cls_name, self.id, self.__dict__)

    def save(self):
        """
        Updates updated_at with the current time when instance is changed.
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance into a dictionary format.

        Returns:
            dict: A dictionary representation of the instance.
        """
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__': str(type(self)).split('.')[-1].split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """
        Deletes the current instance from the storage.
        """
        models.storage.delete(self)
