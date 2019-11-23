"""Some abstracted service layer for appointments"""
import abc

class IAppointmentService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def upsert_appointment(self, appointment):
        """ Create or Update an appointment """
        
    @abc.abstractmethod
    def delete_appointment(self, appointment_id):
        """Delete an existing appointment"""

    @abc.abstractmethod
    def get_all(self):
        """ Get all appointments in the system """

    @abc.abstractmethod
    def get_appointment(self, appointment_id):
        """ Get an appointment through the service

        Args:
            appointment_id: id of the app. to retrieve.
        """

    @abc.abstractmethod
    def get_appointments_for(self, user_id):
        """ Get all the appointments for a given patient"""
        
    @abc.abstractmethod
    def get_appointments_created_by(self, user_id):
        """ Get all the appointments for a given clinician"""
        
    @abc.abstractmethod
    def get_appointments_at_location(self, user_id):
        """ Get all the appointments for a given clinician"""
