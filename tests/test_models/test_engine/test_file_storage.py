import unittest
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City

class TestFileStorage(unittest.TestCase):
    """ Test cases for FileStorage class """

    def test_all(self):
        """ Test all method """
        storage = FileStorage()

        # Create some objects
        state1 = State()
        state2 = State()
        city1 = City()

        # Add objects to storage
        storage.new(state1)
        storage.new(state2)
        storage.new(city1)
        storage.save()

        # Test all method with different parameters
        all_states = storage.all(State)
        self.assertEqual(len(all_states), 2)

        all_objects = storage.all()
        self.assertEqual(len(all_objects), 3)

    def test_delete(self):
        """ Test delete method """
        storage = FileStorage()

        # Create an object
        state = State()

        # Add object to storage
        storage.new(state)
        storage.save()

        # Check that object exists
        self.assertTrue(storage.all(State))

        # Delete the object
        storage.delete(state)

        # Check that object is deleted
        self.assertFalse(storage.all(State))

if __name__ == "__main__":
    unittest.main()
