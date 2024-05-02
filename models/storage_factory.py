#!/usr/bin/python3
"""
This module creates an instance of the appropriate storage engine.
"""

from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

def get_storage():
    """
    Returns an instance of the appropriate storage engine.
    """
    is_type = getenv("HBNB_TYPE_STORAGE")

    if is_type == 'db':
        return DBStorage()
    else:
        return FileStorage()
