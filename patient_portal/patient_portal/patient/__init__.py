"""Init module for the normal users routes"""

from flask import Blueprint

patient = Blueprint('patient', __name__, template_folder='templates')

from . import routes
