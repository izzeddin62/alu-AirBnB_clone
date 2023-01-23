#!/usr/bin/python3
"""base model class"""
import uuid
import datetime


class BaseModel:

    """initialise class"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.createdAt = datetime.datetime.now()
        self.updatedAt = self.createdAt

    """return string representation"""
    def __str__(self):
        dt = "[{}] ({}) {}".format(
                            self.__class__.__name__, self.id, self.__dict__)
        return dt

    """modify the updateAt attribute"""
    def save(self):
        self.updatedAt = datetime.datetime.now()

    """return the dict"""
    def to_dict(self):
        obj = dict(self.__dict__)
        obj["__class__"] = self.__class__.__name__
        obj["createdAt"] = obj["createdAt"].isoformat()
        obj["updatedAt"] = obj["updatedAt"].isoformat()
        return obj
