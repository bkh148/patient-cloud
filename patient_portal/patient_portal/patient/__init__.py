"""Init module for the normal users routes"""

from flask import Blueprint

patient = Blueprint('nuser', __name__)

from . import routes
