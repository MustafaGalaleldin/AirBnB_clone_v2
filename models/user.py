#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column('email', String(128), nullable=False)
        password = Column('password', String(128), nullable=False)
        first_name = Column('first_name', String(128), nullable=True)
        last_name = Column('last_name', String(128), nullable=True)
        places = relationship('Place', backref='user')
        reviews = relationship('Review', backref='user')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
