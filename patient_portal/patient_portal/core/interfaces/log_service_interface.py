""" log service abstraction """

import abc

class ILogService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def log_exception(self, error):
        """build the exception object and log it"""

    @abc.abstractmethod
    def get_exceptions_by_session_id(self, session_id):
        """get all exceptions between two dates"""

    @abc.abstractmethod
    def upsert_exception(self, exception_log):
        """insert or update an exception log"""

    @abc.abstractmethod
    def delete_exception(self, exception_log_id):
        """removes an exception log from the data store"""

    @abc.abstractmethod
    def get_activities_by_session_id(self, session_id):
        """get all activities by session id"""

    @abc.abstractmethod
    def log_activity(self, activity):
        """build the activity object and log it"""

    @abc.abstractmethod
    def upsert_activity(self, activity_log):
        """insert of update an activity log"""

    @abc.abstractmethod
    def delete_activity(self, activity_log_id):
        """removes an activity log from the data store"""
