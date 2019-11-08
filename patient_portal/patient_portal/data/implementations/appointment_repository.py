from ..interfaces import IAppointmentRepository

from datetime import datetime

class AppointmentRepository(IAppointmentRepository):
    """ Some docstring """

    def __init__(self, connection):
        """Initialise"""
        self._connection = connection

    def upsert_appointment(self, payload):
        """ Updates or inserts a new appointment into the datastore.

        Args:
            payload: the appointment object.
        """
        return "upsert appointment"

    def delete_appointment(self, appointment_id):
        """ Deletes an appointment form the datastore.

        Args:
            appointment_id: id of the appointment.
        """
        return "delete appointment"

    def has_appointment(self, appointment_id):
        """ Checks if an appointment exists. """
        return "has appointment"

    def get_appointments_for(self, user_id):
        """ Get appointments created for a user.

        Args:
            user_id: id of the user the appointments are for
        """
        return [{
            "appointment_id" : "aacb69b0-a5f9-4300-9ea5-1713b079ddf5",
            "created_by" : "327d5c97-0c0b-4e3d-86c3-a90f64edb72d",
            "created_for" : "5814ca5c-417c-45db-b6bd-598939b48d75",
            "location_id" : "8ba069ce-a1dc-4687-81b6-8c101e44ade3",
            "created_on_utc": datetime.utcnow(),
            "appointment_date_utc": datetime.utcnow(),
            "appointment_type": "Ultrasound Scan",
            "appointment_notes": "Please make sure to bring the medical records from your last appointment.",
            "is_cancelled": 0,
            "is_attended": 0}]

    def get_appointments_created_by(self, user_id):
        """ Get appointments create by a user.

        Args:
            user_id: id of the user who created the appointments.
        """
        return "get appointment created by"

    def get_appointments_at_location(self, location_id):
        """ Get appointments at a given location.

        Args:
            location_id: id of the location.
        """
        return "get appointment at location"
