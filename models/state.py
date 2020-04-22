#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    state = relationship("City", cascade="all,delete", backref="state")

    @property
    def cities(self):
        """
        Getter attribute for cities
        """
        cities = models.storage.all(City)
        my_list = []
        for key in cities.items():
            if value.state_id == self.id:
                my_list.append(value)
        return my_list
