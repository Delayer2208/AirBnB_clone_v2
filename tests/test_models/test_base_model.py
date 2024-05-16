#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel


class TestBaseModel(test_basemodel):
    """ """

    def test_create_params(self):
        """ """
        new = BaseModel(name="TestModel", number=5)
        self.assertTrue(new.name == "TestModel" and new.number == 5)
