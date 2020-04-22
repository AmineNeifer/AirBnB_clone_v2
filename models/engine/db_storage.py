#!/usr/bin/python3
"""
Db storage
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """
    BDStorage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """initial
        """
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                    user, password, host, database
                    ), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Select all cls
        """
        dic = {}
        if cls is not None:
            query = self.__session.query(cls).all()
            for row in query:
                key = cls.__name__ + '.' + row.id
                dic[key] = row
            return dic
        else:
            lista = ["User", "State", "City", "Amenity", "Place", "Review"]
            for a in lista:
                try:
                    for obj in self.__session.query(eval(a)).all():
                        n = a + '.' + obj.id
                        dic[n] = obj
                except:
                    pass
            return dic

    def new(self, obj):
        """
        add obj to DB
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete obj from DB
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in data base
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(expire_on_commit=False)
        Session = scoped_session(session_factory)
        Session.configure(bind=self.__engine)
        self.__session = Session()

    def close(self):
        self.__session.close()
