#!/usr/bin/python3
"""Console Module"""
import cmd
from models.base_model import BaseModel
from models import storage
import re

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

    def do_create(self, *args):
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
