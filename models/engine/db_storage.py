#!/usr/bin/python3
""" """
from sqlalchemy import create_engine
import os
from base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker



class DBStorage():
    """"""
    __engine = None
    __session = None
    def __init__(self):
        """ """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(os.getenv("HBNB_MYSQL_USER"),
                                              os.getenv("HBNB_MYSQL_PWD"),
                                              os.getenv("HBNB_MYSQL_HOST"),
                                              os.getenv("HBNB_MYSQL_DB")),
                                        pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        
    def all(self, cls=None):
        """ """
        atoo = [User, State, City, Amenity, Place, Review]
        instance_atoo = []
        dictionary = {}

        if cls is None:
            for i in range(len(atoo)):
                instance_atoo += self.__session.query(atoo[i]).all()
        else:
            instance_atoo += self.__session.query(cls).all()

        for i in instance_atoo:
            key = "{}.{}".format(i.__class__.__name__, i.id)
            dictionary[key] = i
        return dictionary

    def new(self, obj):
        """ """
        self.__session.add(obj)

    def save(self):
        """ """
        self.__session.commit()

    def delete(self, obj=None):
        """ """
        if obj not None:
            self.__session.delete(obj)
    
    def reload(self):
        """ """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session
