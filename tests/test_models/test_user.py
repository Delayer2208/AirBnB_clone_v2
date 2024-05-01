"""Test module for User class"""
from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class TestUser(TestBaseModel):
    """Test cases for the User class"""

    def __init__(self, *args, **kwargs):
        """Initialize test instance"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name_type(self):
        """Test type of first_name attribute"""
        instance = self.value()
        self.assertIsInstance(instance.first_name, str)

    def test_last_name_type(self):
        """Test type of last_name attribute"""
        instance = self.value()
        self.assertIsInstance(instance.last_name, str)

    def test_email_type(self):
        """Test type of email attribute"""
        instance = self.value()
        self.assertIsInstance(instance.email, str)

    def test_password_type(self):
        """Test type of password attribute"""
        instance = self.value()
        self.assertIsInstance(instance.password, str)
