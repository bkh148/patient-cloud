import abc

class ISessionService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_session(self, user_id):
        """get a session by the user id"""

    @abc.abstractmethod
    def upsert_session(self, session):
        """update or insert a session object"""

    @abc.abstractmethod
    def delete_session(self, session_id):
        """remove a session from the data store"""

