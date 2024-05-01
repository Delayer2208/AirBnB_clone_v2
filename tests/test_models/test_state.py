"""Test module for State class"""
from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class TestState(TestBaseModel):
    """Test cases for the State class"""

    def __init__(self, *args, **kwargs):
        """Initialize test instance"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name_type(self):
        """Test type of name attribute"""
        instance = self.value()
        self.assertIsInstance(instance.name, str)
