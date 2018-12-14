# --*-- encoding: utf-8 --*--
from __future__ import unicode_literals
from flask import Flask, request, redirect, url_for, flash, render_template
from config import DevelopementConfig

from models import User, Address
from forms import UserCreationForm, AddressForm
from database import db_session

app = Flask(__name__)
app.config.from_object(DevelopementConfig)


@app.route('/users/', methods=['GET', 'POST'])
def show_users():
    """
    A view function to show and add users.
    """
    if request.method == 'POST':
        # If 'post', instantiate the form
        form = UserCreationForm(request.form)
        if form.validate_on_submit():
            flash(message="Success")
            # instantiate the user class
            user = User(first_name=form.first_name.data, last_name=form.last_name.data,
                        email=form.email.data, active=form.active.data,
                        age=form.age.data, gender=form.gender.data,
                        country=form.country.data, state=form.state.data,
                        city=form.city.data, zip_code=form.zip_code.data,
                        timezone=form.timezone.data)
            if user.validate():
                # instantiate the address class
                new_address = Address(address=form.address.data)
                db_session.add(new_address)
                db_session.commit()
                # get and put the address id in the user address_id.
                user.address_id = new_address.id
                db_session.add(user)
                db_session.commit()
                # Redirect to the list of users
                return redirect(url_for('show_users'))
            else:
                # If validation fails, show the form again.
                return render_template('users/users.html', form=form)
        else:
            # If the data in the form is not valid, show the form again.
            return render_template('users/users.html', form=form)
    # If 'GET', show the list of users
    elif request.method == 'GET':
        users = db_session.query(User).all()
        return render_template('users/users.html', users=users)


@app.route('/address/', methods=['GET', 'POST'])
def address():
    """
    A view to display and add addresses.
    """
    form = AddressForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            flash(message="Success")
            new_address = Address(address=form.address.data)
            db_session.add(new_address)
            db_session.commit()
            return redirect(url_for('address'))
        else:
            return render_template('address/address.html', form=form)
    elif request.method == 'GET':
        addresses_lists = db_session.query(Address).all()
        return render_template('address/address.html', addresses=addresses_lists)


@app.route('/')
def home():
    return render_template('home/home.html')


@app.errorhandler(404)
def error_404(error):
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(port=8000)
