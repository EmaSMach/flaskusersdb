# --*-- encoding: utf-8 --*--
from __future__ import unicode_literals

from database import Base
from database import db_session

from utils.validators import validate_email


class Address(Base):
    """
    A simple address data model.
    """
    __table__ = Base.metadata.tables['profiles_address']

    def __str__(self):
        return self.address


class User(Base):
    """
    A user data model.
    """
    users = {}
    fields = ('user_id', 'first_name', 'last_name', 'email', 'active', 'username', 'phone_number',
              'age', 'country', 'state', 'city', 'address', 'zip_code', 'timezone')
    safe_fields = ('id', 'first_name', 'last_name', 'email', 'active', 'phone_number',
                   'age', 'country', 'state', 'city', 'zip_code', 'timezone')
    non_safe_fields = ('address', 'user_id', 'username', 'address',)

    __table__ = Base.metadata.tables['profiles_users']

    def get_address(self):
        """Gets and returns the associated address from the database"""
        return db_session.query(Address).get(self.address_id).address

    @property
    def address(self):
        """Wrapper around get_address method."""
        return self.get_address()

    def to_dict(self):
        """
        Tries to return a dictionary with the fields of the user.
        """
        try:
            local_dict = {field: self.__dict__[field] for field in self.safe_fields}
            local_dict.update({'address': self.address})
            return local_dict
        except TypeError:
            print "Type"
            return None
        except KeyError:
            return None

    def validate(self):
        """
        Validates the fields.
        """
        try:
            assert type(self.first_name) in (str, unicode)
            assert len(self.first_name) != 0
            assert type(self.last_name) in (str, unicode)
            assert len(self.first_name) != 0
            assert validate_email(self.email) is True
            assert self.active in (True, False)
            if self.country:
                assert type(self.country) in (str, unicode)
            if self.state:
                assert type(self.state) in (str, unicode)
            if self.city:
                assert type(self.city) in (str, unicode)
            if self.zip_code:
                assert type(self.zip_code) is int
                assert self.zip_code > 0
            return True
        except AssertionError:
            return False

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)



