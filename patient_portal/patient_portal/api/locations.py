from flask_restplus import Namespace, Resource, fields
from datetime import datetime

nsp = Namespace('locations', description="All location stored within the patient portal system.")


location_fields = nsp.model('Location', {
    'location_id': fields.String(required=True, description="Unique identifier of the location."),
    'name': fields.String(attribute='location_name', required=True, description="Name of the building."),
    'x_coord': fields.Float(attribute='location_coord_x', required=True, description="X coordinate of the location."),
    'y_coord': fields.Float(attribute='location_coord_y', required=True, description="Y coordinate of the location."),
    'address': fields.String(attribute='location_address', required=True, description="Address of the location."),
    'postcode': fields.String(attribute='location_postcode', required=True, description="Postcode of the location."),
    'city': fields.String(attribute='location_city', required=True, description="City of the location.")
})

mock_location = {
    "location_id": "d0e114ba-3527-4c4a-aee7-4bde6095f94f",
    "location_name": "Lancaster's Hospital",
    "location_coord_x": 30.340271,
    "location_coord_y": -152.409757,
    "location_address": "953 Keap Street, 5093",
    "location_postcode": "56",
    "location_city": "Greenwich"
}

locations = [mock_location]

@nsp.route('/')
@nsp.response(200, 'Locations query executed successfully.')
@nsp.response(500, 'Internal server error.')
@nsp.response(403, 'Not authorized.')
class Locations(Resource):
    @nsp.marshal_list_with(location_fields)
    def get(self):
        """Get all locations stored in the patient portal system"""
        try:
            return locations, 200
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
        for location in locations:
            if location['location_id'] == location_id:
                return location
        nsp.abort(404)
        
