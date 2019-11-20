"""Module containing various decorators to be used throughout a flask server"""

from functools import wraps
from .user_roles import UserRole
from flask import request, redirect, url_for, session

def anonymous_required(function):
    @wraps(function)
    def check_anonymous(*args, **kwargs):
        if 'user' in session:
            current_user = session['user']
            for role in UserRole:
                if current_user['role'] == role.value:
                    return redirect(url_for('{}.dashboard'.format(role.value.lower())))
        else:
            return function(*args, **kwargs)
    return check_anonymous


def login_required(role):
    def check_role(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if 'user' in session:
                current_user = session['user']
                if current_user['role'].lower() != role.lower():
                    return redirect(url_for('{}.dashboard'.format(current_user['role'].lower())))
                else:
                    return function(*args, **kwargs)
            else:
                return redirect(url_for('auth.login', next=request.url))    
            return function(*args, **kwargs)
        return wrapper
    return check_role
