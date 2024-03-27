#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base

class DBStorage:
    """This class manages storage of hbnb models in a database"""

    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine and session to communicate with the database"""