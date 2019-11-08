"""Module representing the log repository interface"""

import abc

class ILogRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_exceptions_by_session_id(self, session_id):
        """get all exceptions between two dates"""

    @abc.abstractmethod
    def upsert_exception(self, exception_log):
        """insert or update an exception log"""

    @abc.abstractmethod
    def has_exception(self, exception_log_id):
        """evaluates if an exception log is in the data store"""

    @abc.abstractmethod
    def delete_exception(self, exception_log_id):
        """removes an exception log from the data store"""

    @abc.abstractmethod
    def get_activities_by_session_id(self, session_id):
        """get all activities by session id"""

    @abc.abstractmethod
    def upsert_activity(self, activity_log):
        """insert of update an activity log"""

    @abc.abstractmethod
    def has_activity(self, activity_log_id):
        """evaluates if an activity log is in the data store"""

    @abc.abstractmethod
    def delete_activity(self, activity_log_id):
        """removes an activity log from the data store"""
