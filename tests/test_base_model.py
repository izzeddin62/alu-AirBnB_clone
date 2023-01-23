#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    def test_initialization(self):
        model = BaseModel()
        self.assertEqual(
            str(type(model)), "<class 'models.base_model.BaseModel'>")
        self.assertEqual(str(type(model.id)), "<class 'str'>")
        self.assertEqual(
            str(type(model.createdAt)), "<class 'datetime.datetime'>")
        self.assertEqual(
            str(type(model.updatedAt)), "<class 'datetime.datetime'>")

    def test_string(self):
        model = BaseModel()
        dt = "[{}] ({}) {}".format(
                            model.__class__.__name__, model.id, model.__dict__)
        self.assertEqual(str(model), dt)

    def test_save(self):
        model = BaseModel()
        time = model.updatedAt
        model.save()
        self.assertGreater(model.updatedAt, time)

    def test_dict(self):
        model = BaseModel()
        obj = model.to_dict()
        self.assertEqual(obj["id"], model.id)
        self.assertEqual(obj["__class__"], model.__class__.__name__)
        self.assertEqual(obj["createdAt"], model.createdAt.isoformat())
        self.assertEqual(obj["updatedAt"], model.updatedAt.isoformat())
