"""Some abstracted service layer for appointments"""
import abc

class IAppointmentService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_appointment(self, appointment_id):
        """ Get an appointment through the service

        Args:
            appointment_id: id of the app. to retrieve.
        """

    @abc.abstractmethod
    def get_appointments_for(self, user_id):
        """ Get all the appointments for a given patient        """
