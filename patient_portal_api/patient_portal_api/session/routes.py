""" Module for handling the session HTTP api requests. """

from . import sessions

@sessions.route('/v1.0/', methods=['POST'])
def new_session():
    """Create a new session."""
    return "Create a new session."

@sessions.route('/v1.0/<uuid:session_id>', methods=['GET', 'PATCH', 'DELETE'])
def session_by_id(session_id):
    """Create, Update, Delete session by id."""
    return "Create, Update, Delete session by id. {}".format(session_id)

@sessions.route('/v1.0/collection', methods=['GET'])
def session_collection():
    """Get a collection of sessions.
    """
    return "Get a collection of sessions"
