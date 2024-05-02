#!/usr/bin/python3
"""
This module creates an instance of a FileStorage object.
"""

def get_storage():
    """
    Returns an instance of the appropriate storage engine.
    """
    from os import getenv
    
    is_type = getenv("HBNB_TYPE_STORAGE")

    if is_type == 'db':
        from models.engine.db_storage import DBStorage
        storage = DBStorage()
    else:
        from models.engine.file_storage import FileStorage
        storage = FileStorage()

    storage.reload()
    return storage

storage = get_storage()
