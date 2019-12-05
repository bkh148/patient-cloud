from ..interfaces import ISessionRepository


class SessionRepository(ISessionRepository):

    def __init__(self, db):
        self._db = db

    def get_session(self, user_id):
        """get a session by the user id"""

    def upsert_session(self, session):
        """update or insert a session object"""

    def has_session(self, session_id):
        """evalutate if a session is in the data store"""

    def delete_session(self, session_id):
        """remove a session from the data store"""
