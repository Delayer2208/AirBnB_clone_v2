import os
import unittest
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        # Clear the storage dictionary before each test
        storage._FileStorage__objects = {}

    def tearDown(self):
        """Remove storage file at the end of tests"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_obj_list_empty(self):
        """Test that __objects is initially empty"""
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """Test that a new object is correctly added to __objects"""
        new = BaseModel()
        self.assertIn(new, storage.all().values())

    def test_all(self):
        """Test that __objects is properly returned"""
        new = BaseModel()
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIn(new, all_objects.values())

    def test_base_model_instantiation(self):
        """Test that the file is not created on BaseModel save"""
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """Test that data is saved to the file"""
        new = BaseModel()
        new.save()
        self.assertGreater(os.path.getsize('file.json'), 0)

    def test_save(self):
        """Test the save method of FileStorage"""
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """Test that the storage file is successfully loaded to __objects"""
        new = BaseModel()
        new.save()
        storage.reload()
        loaded_objects = storage.all().values()
        self.assertEqual(new.to_dict(), next(iter(loaded_objects)).to_dict())

    def test_reload_empty(self):
        """Test reloading from an empty file"""
        with open('file.json', 'w'):
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """Test that nothing happens if the file does not exist"""
        self.assertIsNone(storage.reload())

    def test_base_model_save(self):
        """Test that BaseModel save method calls storage save"""
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """Test that __file_path is a string"""
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_type_objects(self):
        """Test that __objects is a dictionary"""
        self.assertIsInstance(storage.all(), dict)

    def test_key_format(self):
        """Test that the key is properly formatted"""
        new = BaseModel()
        obj_id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, f'BaseModel.{obj_id}')

    def test_storage_var_created(self):
        """Test that the FileStorage object 'storage' is created"""
        from models.engine.file_storage import FileStorage
        self.assertIsInstance(storage, FileStorage)
