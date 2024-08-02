#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column('city_id', String(60), ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column('user_id', String(60), ForeignKey('users.id'),
                     nullable=False)
    name = Column('name', String(128), nullable=False)
    description = Column('description', String(1024), nullable=True)
    number_rooms = Column('number_rooms', Integer, nullable=False, default=0)
    number_bathrooms = Column('number_bathrooms', Integer, nullable=False,
                              default=0)
    max_guest = Column('max_guest', Integer, nullable=False, default=0)
    price_by_night = Column('price_by_night', Integer, nullable=False,
                            default=0)
    latitude = Column('latitude', Float, nullable=True)
    longitude = Column('longitude', Float, nullable=True)
    amenity_ids = []
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
    else:
        @property
        def reviews(self):
            """
            getter attribute reviews that returns the list of Review
            instances with place_id equals to the current Place.id
            """
            from models import storage
            from models.review import Review
            ret = []
            for rev in storage.all(Review).values():
                if rev.place_id == self.id:
                    ret.append(rev)
            return ret
