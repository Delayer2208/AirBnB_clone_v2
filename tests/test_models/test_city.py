"""Test module for City class"""
from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class TestCity(TestBaseModel):
    """Test cases for the City class"""

    def __init__(self, *args, **kwargs):
        """Initialize test instance"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id_type(self):
        """Test type of state_id attribute"""
        instance = self.value()
        self.assertIsInstance(instance.state_id, str)

    def test_name_type(self):
        """Test type of name attribute"""
        instance = self.value()
        self.assertIsInstance(instance.name, str)
