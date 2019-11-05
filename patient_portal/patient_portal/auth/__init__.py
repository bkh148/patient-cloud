"""Init module for the auth routes"""

from flask import Blueprint

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

from . import routes
