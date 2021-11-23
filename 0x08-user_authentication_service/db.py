#!/usr/bin/env python3
"""
    Database control class
> Is able to create/delete users
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import User, Base
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """ Database engine class (DB)"""

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        [Summary]
        > Returns a User object that is simultaneously saved
        to the database
        Args:
            email (str): Email for the new user instance
            hashed_password (str): The new hashed password for the instance
        Returns:
            User: Returns a User object
        """
        DBSession = self._session
        new_user = User(email=email, hashed_password=hashed_password)
        DBSession.add(new_user)
        DBSession.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
            Finds a User in the DB based on kwargs:
https://docs.sqlalchemy.org/en/13/orm/query.html#sqlalchemy.orm.query.Query.filter_by
            Returns the first row found in the users table as filtered by
            the method’s input arguments
        """
        DBSession = self._session
        query = DBSession.query(User).filter_by(**kwargs)
        result = query.first()
        if (result is None):
            raise NoResultFound
        return result

    def update_user(self, user_id: int, **kwargs) -> None:
        """
            Updates a user using **kwargs. Returns None.
            Will raise a NoResultFound error if user doesnt exist
            If an attribute is passed that isnt in attributes it will
            raise a ValueError
        """
        DBSession = self._session
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if hasattr(user, key) is False:
                raise ValueError
            setattr(user, key, value)
        DBSession.commit()
