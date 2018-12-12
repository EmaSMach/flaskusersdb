# --*-- encoding: utf-8 --*--
from __future__ import unicode_literals

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, Optional, InputRequired, NumberRange
from wtforms.widgets import TextArea

from utils.validators import PositiveInteger


class UserCreationForm(FlaskForm):
    """
    A simple form to submit user data.
    """
    first_name = StringField('First Name', validators=[
        DataRequired("Field Required"),
        Length(min=3, max=50)
    ])
    last_name = StringField('Last Name', validators=[
        DataRequired(), Length(min=3, max=50)
    ])
    email = StringField('Email', validators=[DataRequired(), Email()])
    active = BooleanField('Active')
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=1)])
    gender = SelectField('Gender', validators=[Optional()], choices=[('', '----'),
                                                                     ('Male', 'Male'),
                                                                     ('Female', 'Female')])
    country = StringField('Country', validators=[Optional()])
    state = StringField('State', validators=[Optional()])
    city = StringField('City', validators=[Optional()])
    address = StringField('Address', widget=TextArea())
    zip_code = IntegerField('Zip Code', validators=[Optional(), PositiveInteger()])
    phone_number = StringField('Phone Number', validators=[Optional()])
    timezone = StringField('Timezone', validators=[Optional()])

    submit = SubmitField("Submit")

    def validate_gender(self, form, field):
        if field == '----':
            self.gender = None


class AddressForm(FlaskForm):
    """
    Simple form for the address.
    """
    address = StringField('Address', validators=[InputRequired(), Length(min=5)])

    submit = SubmitField("Submit")
