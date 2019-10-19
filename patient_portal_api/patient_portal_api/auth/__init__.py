"""Module to expose the authentication RESTful API"""

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import routes
