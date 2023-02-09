#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    """initialise class"""
    def __init__(self):
        super().__init__()