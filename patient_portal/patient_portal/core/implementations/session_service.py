from ..interfaces import ISessionService


class SessionService(ISessionService):

    def __init__(self, repo, log_service):
        self._repo = repo
        self._log_service = log_service

    def get_session(self, user_id):
        """get a session by the user id"""
        return self._repo.get_session(user_id)

    def upsert_session(self, session):
        """update or insert a session object"""
        self._repo.upsert_session(session)

    def delete_session(self, session_id):
        """remove a session from the data store"""
        self._repo.delete_session(session_id)
