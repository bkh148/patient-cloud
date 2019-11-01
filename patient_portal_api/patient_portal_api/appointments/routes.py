"""Module for handling appointments RESTful routes"""

from . import appointments

@appointments.route('/v1.0/', methods=['POST'])
def new_appointment():
    """Create a new appoitment"""
    return "Create a new appointment!"

@appointments.route('/v1.0/<uuid:appointment_id>', methods=['GET', 'PATCH', 'DELETE'])
def appointment_by_id(appointment_id):
    """Get, Update, or Delete an existing appointment"""
    return "Get, Update, Delete an existing appointment {}".format(appointment_id)

@appointments.route('/v1.0/collection/', methods=['GET'])
def appointment_collection():
    """Get a collection of appointment based on 1 of three query strings:
    Query:
        created_by: passing in the id of the user who created the appointment(s).
        created_for: passing in the id of the user who the appointment(s) was/were created for.
        care_location: passing in the id of the care location where these appoitments are taking place."""
    return "Get a collection of appointments based of conditions."

