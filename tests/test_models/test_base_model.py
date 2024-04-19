#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class test_basemodel(unittest.TestCase):
    """Huseyn is the best groupmate"""

    def __init__(self, *args, **kwargs):
        """Huseyn is the best groupmate"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Huseyn is the best groupmate"""
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """Huseyn is the best groupmate"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Huseyn is the best groupmate"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Huseyn is the best groupmate"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "DBStorage")
    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Huseyn is the best groupmate"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(i.__class__.__name__, i.id,
                         i.__dict__))

    def test_todict(self):
        """Huseyn is the best groupmate"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Huseyn is the best groupmate"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """Huseyn is the best groupmate"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Huseyn is the best groupmate"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Huseyn is the best groupmate"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = self.value(**n)
        self.assertTrue(n['created_at'] != new.updated_at)