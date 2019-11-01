""" Module for handling the location HTTP api requests. """

from . import locations

@locations.route('/v1.0/', methods=['POST'])
def new_location():
    """Create a new location."""
    return "Create a new location."

@locations.route('/v1.0/<uuid:location_id>', methods=['GET', 'PATCH', 'DELETE'])
def location_by_id(location_id):
    """Create, Update, Delete location by id."""
    return "Create, Update, Delete location by id. {}".format(location_id)

@locations.route('/v1.0/collection', methods=['GET'])
def location_collection():
    """Get a collection of locations.
    """
    return "Get a collection of location"
