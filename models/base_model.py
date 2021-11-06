#!/usr/bin/python3
"""This module creates a BaseModel class"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
  def __init__(self, *args, **kwargs):
    self.id = str(uuid4())
    self.created_at = datetime.today()
    self.update_at = datetime.today()

    format = "%Y-%m-%dT%H:%M:%S.%f"

    if len(kwargs) != 0:
      for ky, val in kwargs.items():
        if ky == "created_at" or ky == "updated_at":
          self.__dict__[ky] = datetime.strptime(val, format)
        else:
          self.__dict__[ky] =  val

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
    return "[{}] ({}) {}".format( classname,self.id, self.__dict__)