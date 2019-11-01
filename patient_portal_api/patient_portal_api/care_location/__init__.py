"""Module to expose the care locations RESTful API"""

from flask import Blueprint

carelocations = Blueprint('carelocations', __name__)

from . import routes
