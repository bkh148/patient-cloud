"""Module representing the authentication routes"""

from flask import render_template, flash, request, redirect, url_for
from . import auth

# If authenticated, navigated to appropriate view (admin / norm)
#@auth.routes('/', methods=['GET', 'POST'])

# If user is already logged in, redirect to dashboard
@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Endpoint for handling user login."""

    validation_errors=[]

    if request.method == "POST":
        user_id = request.form.get('email', None)
        user_pwd = request.form.get('password', None)

        if user_id == 'liam.j.lamb@gmail.com' and user_pwd == 'Password1':
            return redirect('/admin')
        else:
            validation_errors=['Unrecognised authentication combination.']

    return render_template('auth/login.html', title='Login', static_folder='auth.static', script_paths=['js/auth.js'], style_paths=['css/auth.css'], errors=validation_errors)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """Endpoint for handling user registration."""
    return "Hello, sign up!"

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    """Endpoint for handling user logout."""
    return "Hello, logout!"
