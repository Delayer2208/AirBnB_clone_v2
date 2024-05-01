import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_name(self):
        """Test if name attribute is correctly set"""
        amenity = Amenity(name="Wifi")
        self.assertEqual(amenity.name, "Wifi")


if __name__ == "__main__":
    unittest.main()
