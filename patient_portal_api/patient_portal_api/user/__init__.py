"""Module to expose the users RESTful API"""

from flask import Blueprint

users = Blueprint('users', __name__)

from . import routes
