"""Module to expose the appointments RESTful API"""

from flask import Blueprint

appointments = Blueprint('appointments', __name__)

from . import routes
