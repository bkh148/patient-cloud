"""Handlin the import of the Clinician module"""

from flask import Blueprint

clinician = Blueprint('clinician', __name__, template_folder='templates')

from . import routes
