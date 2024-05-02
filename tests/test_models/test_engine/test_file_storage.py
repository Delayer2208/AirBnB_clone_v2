#!/usr/bin/python3
""" Module for testing file storage"""

import unittest
import os
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_delete(self):
        """ Test delete method """
        new = BaseModel()
        key = "{}.{}".format(new.__class__.__name__, new.id)
        storage.delete(new)
        self.assertNotIn(key, storage._FileStorage__objects)

    def test_all_filtered(self):
        """ Test all method with filtering """
        new1 = BaseModel()
        new2 = BaseModel()
        filtered = storage.all(BaseModel)
        self.assertEqual(len(filtered), 2)
        self.assertIn(new1, filtered.values())
        self.assertIn(new2, filtered.values())


if __name__ == '__main__':
    unittest.main()
