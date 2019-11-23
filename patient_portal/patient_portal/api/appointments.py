from flask_restplus import Namespace, Resource, fields, reqparse
from flask import request
from .. import services
from .locations import location_fields
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity

nsp = Namespace('appointments', description="Accessing appointments created throughout the system.")

appointment_field = nsp.model('Appointment', {
    'appointment_id': fields.String(required=True,  description="The appointment's unique identifier."),
    'created_by': fields.String(required=True, description="Unique identifier of the user having created the appointment."),
    'created_for': fields.String(required=True, description="Unique identifier of the user this appointment was created for."),
    'location_id': fields.String(required=True),
    'created_on_utc': fields.DateTime(required=True),
    'appointment_date_utc': fields.DateTime(required=True),
    'appointment_type': fields.String(required = True),
    'appointment_notes': fields.String(required = True),
    'is_cancelled': fields.Boolean,
    'is_attended': fields.Boolean
})

appointment_parser = reqparse.RequestParser()
appointment_parser.add_argument('Authorization', type=str, required=True, location='headers', help="The user's access_token stored in the context manager.")
appointment_parser.add_argument('appointment_id', type=str, required=True)

@nsp.route('/')
@nsp.response(200, 'Appointments query executed successfully.')
@nsp.response(400, 'Invalid appointment object.')
@nsp.response(500, 'Internal server error.')
@nsp.response(403, 'Not authorized.')
class Appointments(Resource):
    @nsp.marshal_list_with(appointment_field)
    def get(self):
        """ Get all appointments """
        try:
            return services.appointment_service().get_all(), 200
        except Exception as e:
            nsp.abort(500, "An internal error has occurred: {}".format(e))
    
    @nsp.doc(body=appointment_field, response={201: 'Appointment successfully created.'})
    def post(self):
        """ Post a new appointment """
        try:
            appointment = request.json
            services.appointment_service().upsert_appointment(appointment)
            return {'message': 'Successfully added appointment.'}, 201
        except Exception as e:
            nsp.abort(500, "An internal error has occurred: {}".format(e))
            
@nsp.route('/clinician/<string:user_id>')
@nsp.response(200, 'Appointments query executed successfully.')
@nsp.response(400, 'Invalid appointment object.')
@nsp.response(500, 'Internal server error.')
@nsp.response(403, 'Not authorized.')
class AppointmentsCreatedBy(Resource):
    @nsp.marshal_with(appointment_field)
    def get(self, user_id):
        """Get all appointments created by a given user."""
        try:
            return services.appointment_service().get_appointments_created_by(user_id), 200
        except Exception as e:
            nsp.abort(500, "An internal error has occurred: {}".format(e))
        
@nsp.route('/patient/<string:user_id>')
@nsp.response(200, 'Appointments query executed successfully.')
@nsp.response(400, 'Invalid appointment object.')
@nsp.response(500, 'Internal server error.')
@nsp.response(403, 'Not authorized.')
class AppointmentsCreatedFor(Resource):
    @nsp.marshal_with(appointment_field)
    def get(self, user_id):
        """Get all appointments created for a given user."""
        try:
            return services.appointment_service().get_appointments_for(user_id), 200
        except Exception as e:
            nsp.abort(500, "An internal error has occurred: {}".format(e))

# @nsp.route('/<string:location_id>')
# @nsp.response(200, 'Appointments query executed successfully.')
# @nsp.response(400, 'Invalid appointment object.')
# @nsp.response(500, 'Internal server error.')
# @nsp.response(403, 'Not authorized.')
# class AppointmentsAtLocation(Resource):
#     #@nsp.doc(body=appointments_field)
#     @nsp.marshal_list_with(appointment_field)
#     def get(self, location_id):
#         """Get all appointments created at a given location."""
#         try:
#             return [], 200
#         except Exception as e:
#             nsp.abort(500, "An internal error has occurred: {}".format(e))
    
@nsp.route('/<string:appointment_id>')
@nsp.param('appointment_id', "The appointment's unique identifier.")
@nsp.expect(appointment_parser)
@nsp.response(400, 'Invalid appointment object.')
@nsp.response(500, 'Internal server error.')
@nsp.response(403, 'Not authorized.')
class Appointment(Resource):
    @nsp.doc(responses={200: 'Appointment found successfully.'})
    @nsp.marshal_with(appointment_field)
    def get(self, appointment_id):
        """Get an appointment by it's unique identifier"""
        try:
            appointment = services.appointment_service().get_appointment(appointment_id)
            
            if appointment:
                return appointment

            nsp.abort(400, details="Please make sure you provide a valid appointment id (uuid)")
        except Exception as e:
            nsp.abort(500, "An internal error has occurred: {}".format(e))
        
    @nsp.doc(responses={204: 'Appointment updated successfully.'}, body=appointment_field)
    def put(self, appointment_id):
        """Update an appointment by it's unique identifier"""
        
    @nsp.doc(responses={202: 'Appointment has been flagged for deletion.'})
    def delete(self, appointment_id):
        """Flag an appointment for deletion by it's id"""
        try:
            return 202
            #nsp.abort(400, "There was no appointment found at the provided id: {}".format(appointment_id), details="Please make sure you provide a valid appointment id (uuid)")
        except Exception as e:
            nsp.abort(500, "An internal error has occurred: {}".format(e))
    