"""Module for handling appointments RESTful routes"""

from . import appointments

@appointments.route('/v1', methods=['GET'])
def user_appointments():
    """Method for getting all the relevant appointments"""
    return "Hello, API appointments!"
