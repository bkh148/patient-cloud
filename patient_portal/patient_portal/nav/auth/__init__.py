"""Init module for the auth routes"""

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import routes
