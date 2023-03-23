#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.review import Review


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    places = relationship("Place", backref="user", cascade="all, delete")
    reviews = relationship("Place", backref="user", cascade="all, delete")

    @property
    def reviews(self):
        """getter method for cities"""
        review = []

        for reviews in self.E+Review:
            if Review.place_id == self.id:
                review.append(Review)
        return review
