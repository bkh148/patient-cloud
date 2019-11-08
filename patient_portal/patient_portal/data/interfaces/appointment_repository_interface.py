import abc

class IAppointmentRepository(metaclass=abc.ABCMeta):
    """Abstract interface of the appointment repository. This should be used as part of a decoupling process to improve testability and growth of the code."""

    @abc.abstractmethod
    def upsert_appointment(self, payload):
        """ Updates or inserts a new appointment into the datastore.

        Args:
            payload: the appointment object.
        """

    @abc.abstractmethod
    def delete_appointment(self, appointment_id):
        """ Deletes an appointment form the datastore.

        Args:
            appointment_id: id of the appointment.
        """

    @abc.abstractmethod
    def has_appointment(self, appointment_id):
        """ Checks if an appointment exists. """


    @abc.abstractmethod
    def get_appointments_for(self, user_id):
        """ Get appointments created for a user.

        Args:
            user_id: id of the user the appointments are for
        """

    @abc.abstractmethod
    def get_appointments_created_by(self, user_id):
        """ Get appointments create by a user.

        Args:
            user_id: id of the user who created the appointments.
        """

    @abc.abstractmethod
    def get_appointments_at_location(self, location_id):
        """ Get appointments at a given location.

        Args:
            location_id: id of the location.
        """
