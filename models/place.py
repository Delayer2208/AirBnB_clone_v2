#!/usr/bin/python3
"""Place Module for the HBNB project"""

from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
import models
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table

if models.is_type == "db":
    relationship_table = Table('place_amenity', Base.metadata,
                               Column('place_id', String(60),
                                      ForeignKey('places.id'),
                                      nullable=False),
                               Column('amenity_id', String(60),
                                      ForeignKey('amenities.id'),
                                      nullable=False))

class Place(BaseModel, Base):
    """
    The Place class represents a place to stay in the HBNB project.

    Attributes:
        city_id (str): The ID of the city where the place is located.
        user_id (str): The ID of the user who owns the place.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests allowed in the place.
        price_by_night (int): The price per night for the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        reviews (relationship): Relationship to the Review class.
        amenities (relationship): Relationship to the Amenity class.
        amenity_ids (list): List of amenity IDs associated with the place.
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', backref='place', cascade='delete')
    amenities = relationship('Amenity', secondary=relationship_table,
                             viewonly=False)
    amenity_ids = []

    if models.is_type != 'db':
        @property
        def reviews(self):
            """Property to retrieve place reviews."""
            review_values = models.storage.all(Review).values()
            return {review for review in review_values if review.place_id == self.id}

        @property
        def amenities(self):
            """Property to retrieve place amenities."""
            amenity_values = models.storage.all(Amenity).values()
            return [amenity for amenity in amenity_values if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            """Setter method for amenities."""
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
