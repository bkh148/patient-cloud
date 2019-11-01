"""Init module for the admin package."""

from flask import Blueprint

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')

from . import routes
