"""Module representing the authentication routes"""

from flask import render_template, flash, session, request, redirect, url_for, json, make_response
from . import auth
import uuid
from .. import services
from ..core.models import UserRole, anonymous_required

# If authenticated, navigated to appropriate view (admin / norm)
# @auth.routes('/', methods=['GET', 'POST'])

# If user is already logged in, redirect to dashboard
@auth.route('/login', methods=['GET', 'POST'])
@anonymous_required
def login():
    """Endpoint for handling user login."""

    validation_error = {}

    if request.method == "POST":

        user_mail = request.form.get('email', None)
        user_pwd = request.form.get('password', None)
        user = services.user_service().validate_user(user_mail, user_pwd)

        if user:
            session['user'] = user
            for role in UserRole:
                if user['role'] == role.value:
                    session['session_id'] = str(uuid.uuid4())
                    return redirect(url_for('{}.dashboard'.format(role.value.lower())))
                else:
                    validation_error['authentication_error'] = 'An error has occurred logging you in.'
        else:
            validation_error['authentication_error'] = 'Unrecognized e-mail & password combination.'

    return render_template('auth/login.html',
                           title='Login',
                           static_folder='auth.static',
                           script_paths=['js/auth.js'],
                           style_paths=['css/auth.css'],
                           error=validation_error)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """Endpoint for handling user registration."""
    return "Hello, sign up!"


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    """Endpoint for handling user logout."""
    return "Hello, logout!"
