"""Test module for Amenity class"""
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class TestAmenity(TestBaseModel):
    """Test cases for the Amenity class"""

    def __init__(self, *args, **kwargs):
        """Initialize test instance"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name_type(self):
        """Test type of name attribute"""
        new_instance = self.value()
        self.assertIsInstance(new_instance.name, str)
