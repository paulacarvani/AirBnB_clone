#!/usr/bin/python3
""" class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class FileStorage():
    """Private class Atributtes"""
    __file_path = "file.json"
    __objects = {}

    """Public instance Method"""

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        ky = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ky, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        ob_dict = FileStorage.__objects
        obj_dict = {obj: ob_dict[obj].to_dict() for obj in ob_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                obj_dict = json.load(json_file)
                for i in obj_dict.items():
                    nam = i["__class__"]
                    del i["__class__"]
                    self.new(eval(nam)(**i))
        except FileNotFoundError:
            return
