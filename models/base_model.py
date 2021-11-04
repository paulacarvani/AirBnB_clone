#!/usr/bin/python3
"""This module creates a BaseModel class"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
      self.id = str(uuid4())
      self.created_at = datetime.today()
      self.update_at = datetime.today()

    def save(self):
      self.updated_at = datetime.today()

    def to_dict(self):
      ret_dict = self.__dict__.copy()
      ret_dict["__class__"] = self.__class__.__name__
      ret_dict["created_at"] = self.created_at.isoformat()
      ret_dict["update_at"] = self.update_at.isoformat()
      return ret_dict

    def __str__(self):
      classname = self.__class__.__name__
      return "{} {} {}".format( classname,self.id, self.__dict__)
