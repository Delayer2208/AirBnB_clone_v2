"""
This module defines a class for managing database storage
for the HBNB clone
"""
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import models


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """
        Creates an instance of database storage to create the engine
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB"),
                                             pool_pre_ping=True))

        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries the current database session
        """
        if not cls:
            data_list = self.__session.query(Amenity).all()
            data_list.extend(self.__session.query(City).all())
            data_list.extend(self.__session.query(Place).all())
            data_list.extend(self.__session.query(Review).all())
            data_list.extend(self.__session.query(State).all())
            data_list.extend(self.__session.query(User).all())
        else:
            data_list = self.__session.query(cls).all()
        return {'{}.{}'.format(type(obj).__name__, obj.id): obj
                for obj in data_list}

    def new(self, obj):
        """
        Method to add the object to the
        current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Method to commit all changes from the
        current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Method to delete obj from the
        current database session if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Call the remove() method on the private session attribute
        """
        self.__session.close()
