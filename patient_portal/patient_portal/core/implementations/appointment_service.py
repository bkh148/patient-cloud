""" Some implementation of the appointment layer service """

from ..interfaces import IAppointmentService
from ...data.interfaces import IAppointmentRepository

class AppointmentService(IAppointmentService):
    """Implementation of the appointment service abstraction"""

    def __init__(self, repo, log_service):
        """ Some constructor """
        self._repo = repo
        self._log_service = log_service

    def upsert_appointment(self, appointment):
        """ Create or Update an appointment """
        try:
            self._repo.upsert_appointment(appointment)
        except Exception as e:
            self._log_service.log_exception(e)
            raise
        
    def delete_appointment(self, appointment_id):
        """Delete an existing appointment"""
        try:
            self._repo.delete_appointment(appointment_id);
        except Exception as e:
            self._log_service.log_exception(e)
            raise

    def get_all(self):
        """ Get all appointments in the system """
        try:
            return self._repo.get_all()
        except Exception as e:
            self._log_service.log_exception(e)
            raise

    def get_appointment(self, appointment_id):
        """ Get an appointment through the service
        Args:
            appointment_id: id of the app. to retrieve.
        """
        try:
            return self._repo.get_appointments_for(appointment_id)
        except Exception as e:
            self._log_service.log_exception(e)
            raise
        
        return None

    def get_appointments_for(self, user_id):
        """ Get all the appointments for a given user """
        try:
            return self._repo.get_appointments_for(user_id)
        except Exception as e:
            self._log_service.log_exception(e)
            raise
        return []
    
    def get_appointments_created_by(self, user_id):
        """ Get all the appointments for a given clinician"""
        try:
            return self._repo.get_appointments_created_by(user_id)
        except Exception as e:
            self._log_service.log_exception(e)
            raise
            
        return []
        
    def get_appointments_at_location(self, user_id):
        """ Get all the appointments for a given clinician"""
        try:
            return []
        except Exception as e:
            self._log_service.log_exception(e)
            raise
            
        return []
