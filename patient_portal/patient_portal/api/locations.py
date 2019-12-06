from flask_restplus import Namespace, Resource, fields
from flask import request
from datetime import datetime
from patient_portal import services

nsp = Namespace('locations', description="All location stored within the patient portal system.")


location_fields = nsp.model('Location', {
    'location_id': fields.String(required=True, description="Unique identifier of the location."),
    'location_name': fields.String(required=True, description="Name of the building."),
    'location_coord_x': fields.Float(required=True, description="X coordinate of the location."),
    'location_coord_y': fields.Float(required=True, description="Y coordinate of the location."),
    'location_address': fields.String(required=True, description="Address of the location."),
    'location_postcode': fields.String(required=True, description="Postcode of the location."),
    'location_city': fields.String(required=True, description="City of the location.")
})

@nsp.route('/')
@nsp.response(200, 'Locations query executed successfully.')
@nsp.response(500, 'Internal server error.')
@nsp.response(403, 'Not authorized.')
class Locations(Resource):
    @nsp.marshal_list_with(location_fields)
    def get(self):
        """Get all locations stored in the patient portal system"""
        try:
            return services.location_service().get_all_locations() , 200
        except Exception as e:
            nsp.abort(500, "An internal server error has occurred: {}".format(e))
            
    @nsp.doc(body=location_fields, response={201: 'Location successfully created.'})
    def post(self):
        """Add a new location to the platform"""
        try:
            services.location_service().upsert_location(request.json)
        except Exception as e:
            nsp.abort(500, "An internal server error has occurred: {}".format(e))
            

@nsp.route('/<string:location_id>')
@nsp.param('location_id', "The location's unique identifier.")
@nsp.response(404, 'Location not found.')
class Location(Resource):
    @nsp.doc('Get Location')
    @nsp.marshal_with(location_fields)
    def get(self, location_id):
        """Get a location by it's unique identifier"""
        try:
            return services.location_service().get_location_by_id(location_id)
        except Exception as e:
            nsp.abort(500, "An internal server error has occurred: {}".format(e))
