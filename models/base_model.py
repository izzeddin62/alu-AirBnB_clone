#!/usr/bin/python3
"""base model class"""
import uuid
import datetime


class BaseModel:

    """initialise class"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    """return string representation"""
    def __str__(self):
        dt = "[{}] ({}) {}".format(
                            self.__class__.__name__, self.id, self.__dict__)
        return dt

    """modify the updateAt attribute"""
    def save(self):
        self.updated_at = datetime.datetime.now()

    """return the dict"""
    def to_dict(self):
        obj = dict(self.__dict__)
        obj["__class__"] = self.__class__.__name__
        obj["created_at"] = obj["created_at"].isoformat()
        obj["updated_at"] = obj["updated_at"].isoformat()
        return obj
