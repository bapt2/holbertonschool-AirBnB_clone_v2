#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City



class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)
    __tablename__ = 'states'
    cities = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):
        """ """
        cityl= []
        cities = storage.all(City)
        for city in cities.values():
            if self.id == city.state_id:
                cityl.appent(city)
        return cityl