"""Module for handling the import of the local admin"""

from flask import Blueprint

local_admin = Blueprint('local_admin', __name__)

from . import routes
