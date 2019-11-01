"""Module to expose the logs RESTful API"""

from flask import Blueprint

logs = Blueprint('logs', __name__)

from . import routes
