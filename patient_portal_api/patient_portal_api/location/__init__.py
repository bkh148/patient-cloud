"""Module to expose the locations RESTful API"""

from flask import Blueprint

locations = Blueprint('locations', __name__)

from . import routes
