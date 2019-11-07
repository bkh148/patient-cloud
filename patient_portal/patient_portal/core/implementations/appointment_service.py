""" Some implementation of the appointment layer service """

from ..interfaces import IAppointmentService
from ...data.interfaces import IAppointmentRepository

class AppointmentService(IAppointmentService):
    """Implementation of the appointment service abstraction"""

    def __init__(self, repo):
        """ Some constructor """
        self._appointment_repository = repo
        print("SERVICE : Appointment")


    def get_appointment(self, appointment_id):
        """ Get an appointment through the service

        Args:
            appointment_id: id of the app. to retrieve.
        """
        return self._appointment_repository.get_appointments_created_for(appointment_id)
