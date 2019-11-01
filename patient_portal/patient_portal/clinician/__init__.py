"""Handlin the import of the Clinician module"""

from flask import Blueprint

clinician = Blueprint('clinician', __name__)

from . import routes
