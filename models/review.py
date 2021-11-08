#!/usr/bin/python3
"""class review that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review Public class attributes"""
    place_id = ""
    user_id = ""
    text = ""
