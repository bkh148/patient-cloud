"""Module to expose the session RESTful API"""

from flask import Blueprint

sessions = Blueprint('sessions', __name__)

from . import routes
