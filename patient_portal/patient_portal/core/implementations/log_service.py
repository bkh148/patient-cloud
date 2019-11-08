""" Implementation of the log service abstraction """

from ..interfaces import ILogService

class LogService(ILogService):

    def __init__(self, repo):
        self._repo = repo

    def get_exceptions_by_session_id(self, session_id):
        """get all exceptions from a given user session

        Args:
            session_id: user session to retrieve exceptions for.

        Returns:
            empty [] or [] of exceptions.
        """
        return self._repo.get_exceptions_by_session_id(session_id)

    def upsert_exception(self, exception_log):
        """inserts or updates an exception log

        Args:
            exception_log: a full log object to either insert or update appropriately.
        """
        self._repo.upsert_exception(exception_log)

    def delete_exception(self, exception_log_id):
        """removes an exception log from the data store"""
        self._repo.delete_exception(exception_log_id)

    def get_activities_by_session_id(self, session_id):
        """get all activities from a given user session

        Args:
            session_id: user session to retrieve activities for.

        Returns:
            empty [] or [] of activities.
        """
        return self._repo.get_activities_by_session_id(session_id)

    def upsert_activity(self, activity_log):
        """insert of update an activity log"""
        self._repo.upsert_activity(activity_log)

    def delete_activity(self, activity_log_id):
        """removes an activity log from the data store"""
        self._repo.delete_activity(activity_log_id)
