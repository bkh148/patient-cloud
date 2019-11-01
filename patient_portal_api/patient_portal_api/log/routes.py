""" Module for handling the loggin api requests """

from . import logs

@logs.route('/v1.0/activity/', methods=['POST'])
def new_activity():
    """Create a new activity log"""
    return "Create a new activity log"

@logs.route('/v1.0/activity/<uuid:activity_log_id>', methods=['GET', 'PATCH', 'DELETE'])
def activity_log_by_id(activity_log_id):
    """Get, Update, Delete an activity log by id"""
    return "Get, Update, Delete an activity log by id. {}".format(activity_log_id)

@logs.route('/v1.0/activity/collection', methods=['GET'])
def activity_collection():
    """Get a collection of activity logs based on conditions
    Query:
       session_id: Get all activity logs by session id.
       user_id: Get all activity logs by user id.
    """
    return "Get all activity logs for a given session or user."

@logs.route('/v1.0/exception/', methods=['POST'])
def new_exception():
    """Create a new exception log"""
    return "Create a new exception log."

@logs.route('/v1.0/exception/<uuid:exception_log_id>', methods=['GET', 'PATCH', 'DELETE'])
def exception_by_id(exception_log_id):
    """Get, Update, Delete an exception log by id"""
    return "Get, Update, Delete an exception log {}".format(exception_log_id)

@logs.route('/v1.0/exception/collection', methods=['GET'])
def exception_collection():
    """Get a collection of exception logs based on conditions
    Query:
        session_id: Get all the exception logs for a given session.
        user_id: Get all exception logs for a given user.
    """
    return "Get all exceptions for a given user or session"
