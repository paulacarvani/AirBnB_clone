#!/usr/bin/python3
""" class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances"""
from models.base_model import BaseModel
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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        for key, value in FileStorage.__objects.items():
            if not isinstance(value, dict):
                FileStorage.__objects[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") \
             as json_file:
            json.dump(FileStorage.__objects, json_file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                dir_obj = json.load(json_file)
                for i in dir_obj.items():
                    nam = i["__class__"]
                    del i["__class__"]
                    self.new(eval(nam)(**i))
        except FileNotFoundError:
            pass
