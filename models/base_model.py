#!/usr/bin/python3
"""This module creates a BaseModel class"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """class BaseModel that defines all common attributes/methods
    for other classes"""

    def __init__(self, *args, **kwargs):
        """Public instance attributes"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        format = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            """Conditionals for kwargs"""
            for ky, val in kwargs.items():
                if ky == "created_at" or ky == "updated_at":
                    self.__dict__[ky] = datetime.strptime(val, format)
                else:
                    self.__dict__[ky] = val

    def save(self):
        """Public instance method
        updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Public instance method
        returns a dictionary containing all keys/values of
        __dict__ of the instance"""
        ret_dict = self.__dict__.copy()
        ret_dict["__class__"] = self.__class__.__name__
        ret_dict["created_At"] = self.created_at.isoformat()
        ret_dict["updated_at"] = self.updated_at.isoformat()
        return ret_dict

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
