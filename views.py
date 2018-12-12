from forms import UserCreationForm
from flask import request
from models import User, Address


@app.route('/', methods=['GET', 'POST'])
def show_users():
    """
    A view function to show and add users.
    """
    if request.method == 'POST':
        # If 'post', instantiate the form
        form = UserCreationForm(request.form)
        if form.validate_on_submit():
            local_dict = {}
            for field in User.fields:
                local_dict[field] = form[field].data       # Put the data inside the dict
            users.update({form.user_id.data: local_dict})  # Update users dict with the new created local_dict
            flash(message="Success")
            # Redirect to the list of users
            return redirect(url_for('users.show_users'))
        else:
            # If the data in the form is not valid, show the form again.
            return render_template('users/users.html', form=form)
    # If 'GET', show the list of users
    return render_template('users/users.html', users=users.values())