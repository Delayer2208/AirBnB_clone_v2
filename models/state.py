from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

class State(BaseModel, Base):
    """
    The State class represents a state in the HBNB project.

    Attributes:
        name (str): The name of the state.
        cities (relationship): Relationship between State and City.
    """
    if models.is_type == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='delete')

    def __init__(self, *args, **kwargs):
        """
        Initializes a new State instance.

        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        super().__init__(*args, **kwargs)

    if models.is_type != 'db':
        @property
        def cities(self):
            """Getter method for cities"""
            cities_list = []
            all_cities = models.storage.all(City).values()
            for city in all_cities:
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
