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
    'location': fields.Nested(location_fields),
    'created_on_utc': fields.DateTime,
    'appointment_date_utc': fields.DateTime,
    'reason': fields.String(attribute='appointment_type'),
    'notes': fields.String(attribute='appointment_notes'),
    'is_cancelled': fields.Boolean,
    'is_attended': fields.Boolean
})

mockappointment = {
    "appointment_id": "4010b95e-4aba-4183-91f5-db9f13004f4f",
    "created_by": "b4d74b21-2fc9-4567-8b16-59bc0a18fad2",
    "created_for": "2088f26f-0700-4d1c-b4de-f93e9c71d5ee",
    "location": {
        "location_id": "d0e114ba-3527-4c4a-aee7-4bde6095f94f",
        "location_name": "Lancaster's Hosptial",
        "location_coord_x": 30.340271,
        "location_coord_y": -152.409757,
        "location_address": "953 Keap Street, 5093",
        "location_postcode": "56",
        "location_city": "Greenwich"
    },
    "created_on_utc": datetime.utcnow(),
    "appointment_date_utc": datetime.utcnow(),
    "appointment_type": "reprehenderit",
    "appointment_notes": "nisi excepteur ut nulla reprehenderit veniam nostrud labore eu officia minim sit ut amet Lorem magna et velit eiusmod occaecat do laborum aliqua ipsum sit est labore excepteur eu dolor aute labore ullamco exercitation sint proident do quis occaecat est enim culpa et veniam proident est fugiat tempor labore mollit dolor consequat velit sint consectetur ex tempor ex ex laboris laboris excepteur tempor sunt nisi mollit deserunt et ea minim magna deserunt Lorem magna culpa qui id aliqua nostrud fugiat labore incididunt nulla enim laborum excepteur adipisicing esse Lorem sint exercitation exercitation reprehenderit Lorem cupidatat minim sit exercitation mollit laboris",
    "is_cancelled": True,
    "is_attended": False
}


appointments = [mockappointment]

appointment_parser = reqparse.RequestParser()
appointment_parser.add_argument('Authorization', type=str, required=True, location='headers', help="The user's access_token stored in the context manager.")
appointment_parser.add_argument('appointment_id', type=str, required=True)

@nsp.route('/')
@nsp.response(200, 'Appointments query executed successfully.')
@nsp.response(400, 'Invalid appointment object.')
@nsp.response(500, 'Internal server error.')
@nsp.response(403, 'Not authorized.')
class Appointments(Resource):
    #@nsp.doc(body=appointments_field)
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
        appointment = request.json
        return {"appointment": appointment}, 201
        

# @nsp.route('/<string:created_by>')
# @nsp.response(200, 'Appointments query executed successfully.')
# @nsp.response(400, 'Invalid appointment object.')
# @nsp.response(500, 'Internal server error.')
# @nsp.response(403, 'Not authorized.')
# class AppointmentsCreatedBy(Resource):
#     #@nsp.doc(body=appointments_field)
#     @nsp.marshal_list_with(appointment_field)
#     def get(self, created_by):
#         """Get all appointments created by a given user."""
#         try:
#             return [], 200
#         except Exception as e:
#             nsp.abort(500, "An internal error has occurred: {}".format(e))

# @nsp.route('/<string:created_for>')
# @nsp.response(200, 'Appointments query executed successfully.')
# @nsp.response(400, 'Invalid appointment object.')
# @nsp.response(500, 'Internal server error.')
# @nsp.response(403, 'Not authorized.')
# class AppointmentsCreatedFor(Resource):
#     #@nsp.doc(body=appointments_field)
#     @nsp.marshal_list_with(appointment_field)
#     def get(self, created_for):
#         """Get all appointments created for a given user."""
#         try:
#             return [], 200
#         except Exception as e:
#             nsp.abort(500, "An internal error has occurred: {}".format(e))
    
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
    