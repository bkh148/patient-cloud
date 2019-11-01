""" Module for handling the HTTP request for the cate location api"""

from . import carelocations

@carelocations.route('/v1.0/', methods=['POST'])
def new_carelocation():
    """ Create a new carelocation """
    return "Create a new carelocation!"

@carelocations.route('/v1.0/<uuid:care_location_id>', methods=['GET', 'PATCH', 'DELETE'])
def care_location_by_id(care_location_id):
    """ Get, Update, Delete a care location by id."""
    return "Create, Update or Delete a care location. {}".format(care_location_id)

@carelocations.route('/v1.0/collection/', methods=['GET'])
def care_location_collection():
    """ Get all registered care location. """
    return "Get all registered care locations."
