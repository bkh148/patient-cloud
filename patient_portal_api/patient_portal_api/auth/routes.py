"""Module for handling the RESTful API authentication routes"""

from . import auth

@auth.route('/v1', methods=['GET'])
def login():
    """Request for authenticating a user"""
    return "Hello, API login!"
