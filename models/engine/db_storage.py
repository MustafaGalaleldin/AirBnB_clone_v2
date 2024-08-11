#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine import create_engine
from os import getenv
from models.base_model import Base


class DBStorage:
    "database engine class"
    __engine = None
    __session = None

    def __init__(self):
        "Constructor"
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')
        engine_url = "mysql+mysqldb://{}:{}@{}/{}".format(user, passwd, host,
                                                          db_name)
        self.__engine = create_engine(engine_url, pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        "all objects depending of the class name (argument cls)"
        ret = {}
        results = []
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
            if issubclass(cls, Base):
                results = self.__session.query(cls).all()
        else:
            for child in Base.__subclasses__():
                results.extend(self.__session.query(child).all())
        for obj in results:
            ret[f"{obj.__class__.__name__}.{obj.id}"] = obj
        return ret

    def new(self, obj):
        "add the object to the current database session"
        if obj:
            self.__session.add(obj)

    def save(self):
        "commit all changes of the current database session"
        self.__session.commit()

    def delete(self, obj=None):
        "delete from the current database session obj if not None"
        if obj:
            self.__session.delete(obj)

    def reload(self):
        "create all tables in the database"
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        session_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fac)
        self.__session = Session

    def close(self):
        "remove the session"
        self.__session.remove()
