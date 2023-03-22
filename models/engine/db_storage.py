#!/usr/bin/python3
"""This module defines a class to manage DBstorage for hbnb clone"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models to DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """Instatntiates"""

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}?pool_pre_ping=True'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')))
        
        metadata = MetaData(bind=self.__engine)

        if os.getenv('HBNB_ENV') == 'test':
            metadata.drop_all()

    def all(self, cls=None):
        """Returns the list of objects of one type of class"""
        
        res = {}
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
        else:
            classes = [cls]

        for cls in classes:
            objs = self.__session.query(cls)
            for obj in objs.all():
                key = '{}.{}'.format(cls.__name__, obj.id)
                res[key] = obj

        return res    
    
    def new(self, obj):
        """Add the object to the current database session"""
        
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""

        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        
        if obj is not None:
            self.__session.delete(obj)
        
    def reload(self):
        """create all tables in the database"""

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session                    
