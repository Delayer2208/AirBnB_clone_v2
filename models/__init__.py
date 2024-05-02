#!/usr/bin/python3
"""
This module creates an instance of a FileStorage object.
"""
from os import getenv

def get_storage():
    """
    Returns an instance of the appropriate storage engine.
    """
    is_type = getenv("HBNB_TYPE_STORAGE")
    
    if is_type == 'db':
        from models.engine.db_storage import DBStorage
        return DBStorage()
    else:
        from models.engine.file_storage import FileStorage
        return FileStorage()

storage = get_storage()
storage.reload()
