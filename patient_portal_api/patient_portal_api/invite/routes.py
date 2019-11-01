""" Module for handling the invite HTTP api requests. """

from . import invites

@invites.route('/v1.0/', methods=['POST'])
def new_invite():
    """Create a new invite."""
    return "Create a new invite."

@invites.route('/v1.0/<uuid:invite_id>', methods=['GET', 'PATCH', 'DELETE'])
def invite_by_id(invite_id):
    """Create, Update, Delete invite by id."""
    return "Create, Update, Delete invite by id. {}".format(invite_id)

@invites.route('/v1.0/collection', methods=['GET'])
def invite_collection():
    """Get a collection of invites based on a set of conditions.
    Query:
        created_for: Get all invitations created for user by id.
        created_by: Get all invitation created by a user by id.
    """
    return "Get a collection of invites"
