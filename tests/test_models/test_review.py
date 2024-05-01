"""Test module for Review class"""
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review


class TestReview(TestBaseModel):
    """Test cases for the Review class"""

    def __init__(self, *args, **kwargs):
        """Initialize test instance"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id_type(self):
        """Test type of place_id attribute"""
        instance = self.value()
        self.assertIsInstance(instance.place_id, str)

    def test_user_id_type(self):
        """Test type of user_id attribute"""
        instance = self.value()
        self.assertIsInstance(instance.user_id, str)

    def test_text_type(self):
        """Test type of text attribute"""
        instance = self.value()
        self.assertIsInstance(instance.text, str)
