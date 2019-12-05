from ..interfaces import IAppointmentRepository


from pprint import pprint as pp
from datetime import datetime

class AppointmentRepository(IAppointmentRepository):
    """ Some docstring """

    def __init__(self, db):
        """Initialise"""
        self._db = db

    def upsert_appointment(self, appointment):
        """ Updates or inserts a new appointment into the datastore."""
        if self.has_appointment(appointment['appointment_id']):
            self._db.update('appointments', appointment)
        else:
            self._db.insert('appointments', appointment)

    def delete_appointment(self, appointment_id):
        """ Deletes an appointment form the datastore.
        Args:
            appointment_id: id of the appointment.
        """
        self._db.execute("""
            DELETE FROM appointments
            WHERE appointment_id = ?""", (appointment_id, ))

    def has_appointment(self, appointment_id):
        """ Checks if an appointment exists. """
        return self._db.count("""
            SELECT COUNT() FROM appointments
            WHERE appointment_id = ?""", (appointment_id, )) > 0

    def get_all(self):
        """ Get all appointments in the system """
        return self._db.get_all("""
            SELECT * FROM appointments
            ORDER BY date(appointment_date_utc)""")

    def get_appointments_for(self, user_id):
        """ Get appointments created for a user.

        Args:
            user_id: id of the user the appointments are for
        """
        return self._db.get_all("""
        SELECT * FROM appointments
        WHERE created_for = ?
        ORDER BY date(appointment_date_utc)""", (user_id, ))

    def get_appointments_created_by(self, user_id):
        """ Get appointments create by a user.

        Args:
            user_id: id of the user who created the appointments.
        """
        return self._db.get_all("""
        SELECT * FROM appointments
        WHERE created_by = ?
        ORDER BY date(appointment_date_utc)""", (user_id, ))

    def get_appointments_at_location(self, location_id):
        """ Get appointments at a given location.

        Args:
            location_id: id of the location.
        """
        return self._db.get_all("""
        SELECT * FROM appointments
        WHERE location_id = ?
        ORDER BY date(appointment_date_utc)""", (location_id, ))
