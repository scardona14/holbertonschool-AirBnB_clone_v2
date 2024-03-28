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
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                       .format(os.getenv('HBNB_MYSQL_USER'),
                                               os.getenv('HBNB_MYSQL_PWD'),
                                               os.getenv('HBNB_MYSQL_HOST'),
                                               os.getenv('HBNB_MYSQL_DB'),
                                               pool_pre_ping=True))
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        from models import base_model
        objects = {}
        if cls:
            query = self.__session.query(eval(cls))
            for obj in query:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        else:
            for cls in base_model.Base.__subclasses__():
                query = self.__session.query(cls)
                for obj in query:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        return objects
            
    def new(self, obj):
        """Adds new object to storage"""
        self.__session.add(obj)
    
    def save(self):
        """Commits all changes to the database"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Deletes obj from the database"""
        if obj is not None:
            self.__session.delete(obj)
