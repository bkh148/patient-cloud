from ..interfaces import IAppointmentRepository


from pprint import pprint as pp
from datetime import datetime

class AppointmentRepository(IAppointmentRepository):
    """ Some docstring """

    def __init__(self, db):
        """Initialise"""
        self._db = db

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

        return [
            {"appointment_id": "b7693c90-6009-4141-96be-a94cf62f3b84",
             "created_by": "d2623b0a-2b48-49b9-82e3-8743f9254f78",
             "created_for": "e1bbb1b3-9dfc-496d-a62c-c003646b9a46",
             "location_name": "Astley Ainslie Hospital",
             "location_coord_x": "1.21",
             "location_coord_y": "1.21",
             "location_postcode": "EH9 2HL",
             "location_address": "Grange Loan",
             "location_city": "Edinburgh",
             "created_on_utc": datetime.utcnow(),
             "appointment_date_utc": datetime.utcnow(),
             "appointment_type": "Some check-up",
             "appointment_notes": """
             Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
             """,
             "is_cancelled": 0,
             "is_attended": 0},
            {"appointment_id": "",
             "created_by": "d2623b0a-2b48-49b9-82e3-8743f9254f78",
             "created_for": "e1bbb1b3-9dfc-496d-a62c-c003646b9a46",
             "location_name": "Chalmers Hospital",
             "location_coord_x": "1.21",
             "location_coord_y": "1.21",
             "location_postcode": "EH3 9HQ",
             "location_address": "Chalmers Street",
             "location_city": "Edinburgh",
             "created_on_utc": datetime.utcnow(),
             "appointment_date_utc": datetime.utcnow(),
             "appointment_type": "Some check-up",
             "appointment_notes": """
             Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
             """,
             "is_cancelled": 0,
             "is_attended": 0} ,
           {"appointment_id": "",
             "created_by": "d2623b0a-2b48-49b9-82e3-8743f9254f78",
             "created_for": "e1bbb1b3-9dfc-496d-a62c-c003646b9a46",
             "location_name": "Lauriston Building",
             "location_coord_x": "1.21",
             "location_coord_y": "1.21",
             "location_postcode": "EH3 9EN",
             "location_address": "Lauriston Place",
             "location_city": "Edinburgh",
             "created_on_utc": datetime.utcnow(),
             "appointment_date_utc": datetime.utcnow(),
             "appointment_type": "Some check-up",
             "appointment_notes": """
             Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
             """,
             "is_cancelled": 0,
             "is_attended": 0} ]

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
