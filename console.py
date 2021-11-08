#!/usr/bin/python3
"""Console Module"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re

classes = {"BaseModel": BaseModel, "User": User, "State": State,\
    "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, *args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, *args):
        """EOF command to exit the program
        """
        return True

    def emptyline(self) -> bool:
        """shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saveit (to the JSON file)
        and prints the id. Ex: $ create BaseModel
        """
        if not arg:
            print("** class name migging **")
        elif arg not in classes.keys():
            print("** class doesn't exist **")
        else:
            obj = classes[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """ print the string representation of an instance base on the class
        name and id. Ex $ show BaseModel 1234-1234-1234"""
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
if __name__ == '__main__':
    HBNBCommand().cmdloop()
