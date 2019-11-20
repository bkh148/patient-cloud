"""Module for handling appointments RESTful routes"""

from flask import jsonify
from flask_restful import Resource

__all__ = ['Appointment', 'AppointmentCollection']

class Appointment(Resource):
    def get(self, appointment_id):
        return jsonify({'appoinment_id': appointment_id}), 200
    
    def delete(self, appointment_id):
        print('Delete appointment')
        return '', 204
    
    def put(self, appointment_id):
        print("Update appointment")
        return {'appoinment_id': 'udpated'}, 201
    
class AppointmentCollection(Resource):
    def get(self):
        return jsonify([{'appoinment_id': 1}, {'appoinment_id': 2}, {'appoinment_id': 3}]), 200
    
    def post(self):
        print("Add a new appointment")
        return 201

