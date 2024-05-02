import cmd
from models import storage
from models.state import State
from models.city import City

class HBNBCommand(cmd.Cmd):
    """HBNB Command Line Interpreter"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args[0])()
            if args[0] == 'State':
                if len(args) < 2:
                    print("** missing name **")
                    return
                setattr(new_instance, 'name', args[1])
            elif args[0] == 'City':
                if len(args) < 3:
                    print("** missing parameters **")
                    return
                setattr(new_instance, 'name', args[2].replace("_", " "))
                setattr(new_instance, 'state_id', args[1])
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            obj = storage.all()[args[0] + '.' + args[1]]
            print(obj)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            del storage.all()[args[0] + '.' + args[1]]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        objects = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in objects.values()])
        elif args[0] in storage.classes:
            print([str(obj) for obj in objects.values() if type(obj).__name__ == args[0]])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        try:
            obj = storage.all()[args[0] + '.' + args[1]]
            setattr(obj, args[2], args[3])
            obj.save()
        except KeyError:
            print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
