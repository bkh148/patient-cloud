import abc

class ISessionRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_session(self, user_id):
        """get a session by the user id"""

    @abc.abstractmethod
    def upsert_session(self, session):
        """update or insert a session object"""

    @abc.abstractmethod
    def has_session(self, session_id):
        """evalutate if a session is in the data store"""

    @abc.abstractmethod
    def delete_session(self, session_id):
        """remove a session from the data store"""

