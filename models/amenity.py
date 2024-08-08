#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy import Integer, Float, String
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    "Amenities class"
    from models.place import place_amenities
    __tablename__ = 'amenities'
    name = Column('name', String(128), nullable=False)
    place_amenities = relationship('Place', secondary=place_amenities,
                                   overlaps="amenities")
