"""Init module for the admin package."""

from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import routes
