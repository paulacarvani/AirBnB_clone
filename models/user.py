#!/usr/bin/python3
"""class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class User Public class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
