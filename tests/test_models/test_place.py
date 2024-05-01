"""Test module for Place class"""
from tests.test_models.test_base_model import TestBaseModel
from models.place import Place


class TestPlace(TestBaseModel):
    """Test cases for the Place class"""

    def __init__(self, *args, **kwargs):
        """Initialize test instance"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id_type(self):
        """Test type of city_id attribute"""
        instance = self.value()
        self.assertIsInstance(instance.city_id, str)

    def test_user_id_type(self):
        """Test type of user_id attribute"""
        instance = self.value()
        self.assertIsInstance(instance.user_id, str)

    def test_name_type(self):
        """Test type of name attribute"""
        instance = self.value()
        self.assertIsInstance(instance.name, str)

    def test_description_type(self):
        """Test type of description attribute"""
        instance = self.value()
        self.assertIsInstance(instance.description, str)

    def test_number_rooms_type(self):
        """Test type of number_rooms attribute"""
        instance = self.value()
        self.assertIsInstance(instance.number_rooms, int)

    def test_number_bathrooms_type(self):
        """Test type of number_bathrooms attribute"""
        instance = self.value()
        self.assertIsInstance(instance.number_bathrooms, int)

    def test_max_guest_type(self):
        """Test type of max_guest attribute"""
        instance = self.value()
        self.assertIsInstance(instance.max_guest, int)

    def test_price_by_night_type(self):
        """Test type of price_by_night attribute"""
        instance = self.value()
        self.assertIsInstance(instance.price_by_night, int)

    def test_latitude_type(self):
        """Test type of latitude attribute"""
        instance = self.value()
        self.assertIsInstance(instance.latitude, float)

    def test_longitude_type(self):
        """Test type of longitude attribute"""
        instance = self.value()
        self.assertIsInstance(instance.longitude, float)

    def test_amenity_ids_type(self):
        """Test type of amenity_ids attribute"""
        instance = self.value()
        self.assertIsInstance(instance.amenity_ids, list)
