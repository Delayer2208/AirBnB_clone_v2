class FileStorage:
    """ File storage class """

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self, cls=None):
        """ Returns the dictionary """
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        else:
            return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                objects_dict = json.load(file)
                for k, v in objects_dict.items():
                    cls_name = v['__class__']
                    cls = eval(cls_name)
                    self.__objects[k] = cls(**v)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Deletes obj from __objects if it exists """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()
