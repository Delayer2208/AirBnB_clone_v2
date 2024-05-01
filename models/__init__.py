#!/usr/bin/python3
"""
Module to initialize the storage mechanism for the application.

This module creates an instance of either FileStorage or DBStorage based on the
environment variable HBNB_TYPE_STORAGE.
"""

from os import getenv

# Determine the type of storage based on the environment variable
storage_type = getenv("HBNB_TYPE_STORAGE")

# Import either FileStorage or DBStorage based on the storage type
if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Load data into the storage mechanism
storage.reload()
