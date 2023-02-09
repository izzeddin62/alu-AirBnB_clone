#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel
from models import storage

class User(BaseModel):

    """initialise class"""
    def __init__(self, email = "", password = "", first_name = "", last_name = ""):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        storage.new(self)