"""Init module for the normal users routes"""

from flask import Blueprint

nuser = Blueprint('nuser', __name__)

from . import routes
