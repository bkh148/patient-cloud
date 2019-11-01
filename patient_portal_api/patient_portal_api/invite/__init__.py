"""Module to expose the invites RESTful API"""

from flask import Blueprint

invites = Blueprint('invites', __name__)

from . import routes
