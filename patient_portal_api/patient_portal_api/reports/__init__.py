"""Module to expose the reports RESTful API"""

from flask import Blueprint

reports = Blueprint('reports', __name__)

from . import routes
