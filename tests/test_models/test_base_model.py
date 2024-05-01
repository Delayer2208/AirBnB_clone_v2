"""Test module for BaseModel class"""
import unittest
import datetime
from models.base_model import BaseModel
import json
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialize test instance"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up test environment"""
        pass

    def tearDown(self):
        """Tear down test environment"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default_instance(self):
        """Test default instance creation"""
        instance = self.value()
        self.assertIsInstance(instance, self.value)

    def test_kwargs_instance(self):
        """Test instance creation with kwargs"""
        instance = self.value()
        instance_dict = instance.to_dict()
        new_instance = BaseModel(**instance_dict)
        self.assertIsNot(new_instance, instance)

    def test_save_method(self):
        """Test save method"""
        instance = self.value()
        instance.save()
        key = "{}.{}".format(self.name, instance.id)
        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertEqual(data[key], instance.to_dict())

    def test_str_representation(self):
        """Test string representation of instance"""
        instance = self.value()
        expected_output = '[{}] ({}) {}'.format(
            self.name, instance.id, instance.__dict__)
        self.assertEqual(str(instance), expected_output)

    def test_to_dict_method(self):
        """Test to_dict method"""
        instance = self.value()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)

    def test_id_type(self):
        """Test type of id attribute"""
        instance = self.value()
        self.assertIsInstance(instance.id, str)

    def test_created_at_type(self):
        """Test type of created_at attribute"""
        instance = self.value()
        self.assertIsInstance(instance.created_at, datetime.datetime)

    def test_updated_at_type(self):
        """Test type of updated_at attribute"""
        instance = self.value()
        self.assertIsInstance(instance.updated_at, datetime.datetime)

    def test_created_updated_at_difference(self):
        """Test difference between created_at and updated_at"""
        instance = self.value()
        self.assertNotEqual(instance.created_at, instance.updated_at)

    def test_invalid_kwargs_none(self):
        """Test instance creation with invalid kwargs (None)"""
        kwargs = {None: None}
        with self.assertRaises(TypeError):
            new_instance = self.value(**kwargs)

    def test_invalid_kwargs_one(self):
        """Test instance creation with invalid kwargs (one key)"""
        kwargs = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new_instance = self.value(**kwargs)
