"""Init module for the REST API"""

from flask import Blueprint
from flask_restful import Api, Resource, url_for
from .appointments import Appointment, AppointmentCollection

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

api.add_resource(Appointment, '/appointments/<uuid:appointment_id>')
api.add_resource(AppointmentCollection, '/appointments')
