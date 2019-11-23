from flask_restplus import Namespace, Resource, fields, reqparse
from flask import request
from .. import services


nsp = Namespace('logs', description='Accessing patient portal\'s log api.')


# The session id will be added onto the object if applicable.
# The only cases it won't be applicable is if the api is used through swagger interface.
exception_field = nsp.model('Exception', {
    'exception_log_id': fields.String(required=True),
    'exception_log_type': fields.String(required=True),
    'occurred_on_utc': fields.String(required=True),
    'is_handled': fields.Boolean(required=True),
    'stack_trace': fields.String(required=True)
})

# The session id will be added onto the object if applicable.
# The only cases it won't be applicable is if the api is used through swagger interface.
activity_field = nsp.model('Activity', {
    'activity_log_id': fields.String(required=True),
    'activity_log_type': fields.String(required=True),
    'occurred_on_utc': fields.DateTime(required=True)
})

@nsp.route('/exceptions/<string:session_id>')
@nsp.response(400, 'Invalid exception object.')
@nsp.response(500, 'Internal server error')
@nsp.response(403, 'Not authorized')
class ExceptionCollection(Resource):
    @nsp.doc(responses={200: 'Exception log query successfully executed.'})
    @nsp.marshal_list_with(exception_field)
    def get(self, session_id):
        """Get all exception for a given session"""
        try:
            return services.log_service().get_exceptions_by_session_id(session_id)
        except Exception as e:
            nsp.abort(500, "An internal error has occurred: {}".format(e))
            

@nsp.route('/exceptions')
@nsp.response(400, 'Invalid exception object.')
@nsp.response(500, 'Internal server error')
@nsp.response(403, 'Not authorized')
class Exception(Resource):
    @nsp.doc(responses={201: 'Exception log successfully created.'}, body=exception_field)
    @nsp.marshal_with(exception_field)
    def post(self):
        """Insert a new exception log"""
        try:
            exception = request.json
            services.log_service().upsert_exception(exception), 201
        except Exception as e:
            nsp.abort(500, "An internal error has occurred: {}".format(e))
    
    @nsp.doc(responses={204: 'Exception log successfully updated.'})
    @nsp.marshal_with(exception_field)
    def put(self):
        """Update an exception object by it's id."""
        try:
            exception = request.json
            #TODO: push in session id
            services.log_service().upsert_exception(exception), 204
        except Exception as e:
            nsp.abort(500, "An internal error has occurred: {}".format(e))
    
    
@nsp.route('/activities/<string:session_id>')
@nsp.response(400, 'Invalid activity object.')
@nsp.response(500, 'Internal server error')
@nsp.response(403, 'Not authorized')
class ActivityCollection(Resource):
    @nsp.doc(responses={200: 'Activity log query successfully executed.'})
    @nsp.marshal_list_with(activity_field)
    def get(self, session_id):
        """Get all activities for a given session"""
        try:
            return services.log_service().get_activities_by_session_id(session_id)
        except Exception as e:
            nsp.abort(500, "An internal error has occurred: {}".format(e))

@nsp.route('/activities')
@nsp.response(400, 'Invalid exception object.')
@nsp.response(500, 'Internal server error')
@nsp.response(403, 'Not authorized')
class Activity(Resource):
    @nsp.doc(responses={201: 'Activity log successfully created.'}, body=activity_field)
    @nsp.marshal_with(activity_field)
    def post(self):
        """Insert a new activity log"""
        try:
            activity = request.json
            #TODO: push in session id
            services.log_service().upsert_activity(activity), 201
        except Exception as e:
            nsp.abort(500, "An internal error has occurred: {}".format(e))
    
    @nsp.doc(responses={204: 'Activity log successfully updated.'})
    @nsp.marshal_with(activity_field)
    def put(self):
        """Update an activity object by it's id."""
        try:
            activity = request.json
            #TODO: push in session id
            services.log_service().upsert_activity(activity), 204
        except Exception as e:
            nsp.abort(500, "An internal error has occurred: {}".format(e))
