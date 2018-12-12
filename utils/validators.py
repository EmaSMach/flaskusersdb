# --*-- encoding: utf-8 --*--
import re

from wtforms.validators import ValidationError

FIELDS = ('user_id', 'first_name', 'last_name', 'email', 'active', 'username',
          'age', 'country', 'state', 'city', 'address', 'zip_code')


def validate_email(email):
    """
    Checks if the email is valid.
    """
    pattern = re.compile(r"\b[\w.%+-]+@[\w.-]+\.[a-zA-A]{2,6}\b")
    if re.match(pattern, email):
        return True
    else:
        return False


def validate_length(value):
    """
    Checks if value is a string and its length is longer than 3.
    """
    if isinstance(value, (str, unicode)):
        if len(value) >= 3:
            return True
        else:
            return False
    return False


class IsInteger(object):
    """
    Validates the type of the field.
    """
    def __init__(self, message="This filed must contain only integers"):
        self.message = message

    def __call__(self, form, field):
        if field.data:
            try:
                int(field.data)
            except TypeError:
                raise ValidationError(self.message)


class PositiveInteger(object):
    """
    Validates if the number is positive.
    """
    def __init__(self, message="This filed must contain only integers"):
        self.message = message

    def __call__(self, form, field):
        if field.data:
            try:
                int(field.data)
                if int(field.data) <= 0:
                    raise ValidationError("The number should be positive")
            except TypeError:
                raise ValidationError(self.message)

