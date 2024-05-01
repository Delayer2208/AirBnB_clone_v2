import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project"""

    prompt = "(hbnb) "
    file = None

    def do_create(self, arg):
        """Create a new instance of BaseModel and saves it to JSON file"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()

        for param in args[1:]:
            key, value = param.split("=")

            if not value:
                print("** missing attribute value **")
                return

            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]

            setattr(new_instance, key, value)

        new_instance.save()
        print(new_instance.id)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End of File (EOF) command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
