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
    if getenv('HBNB_TYPE_STORAGE') == 'db':
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
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenities,
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        "initialzing"
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """getter attribute returns the list of Review instances"""
            from models.review import Review
            review_list = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """getter attribute returns the list of Amenity instances"""
            from models.amenity import Amenity
            amenity_list = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list
