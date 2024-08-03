#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy import Integer, Float, String
from sqlalchemy.orm import relationship
from os import getenv

metadata = Base.metadata
place_amenities = Table('place_amenities', metadata,
                        Column('place_id', String(60), ForeignKey('places.id'),
                               primary_key=True, nullable=False),
                        Column('amenity_id', String(60),
                               ForeignKey('amenities.id'), primary_key=True,
                               nullable=False))


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
        amenities = relationship('Amenity', secondary=place_amenities,
                                 viewonly=False)
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

        @property
        def amenities(self):
            """
            returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place
            """
            from models import storage
            from models.amenity import Amenity
            amenities_list = list(storage.all(Amenity).values())
            return [a for a in amenities_list if a.id in self.amenity_ids]
