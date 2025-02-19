#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade='all, delete-orphan')

    @property
    def cities(self):
        """Return a list with the citites"""
        city_dict = models.storage.all(City)
        city_list = []
        for key, value in city_dict.items():
            if value.state_id == self.id:
                city_list.append(value)
        return city_list
