""" Implementation of the log service abstraction """
from flask import session
from ..interfaces import ILogService
import traceback, uuid
from datetime import datetime
from ..models.exception_types import ExceptionType
from pprint import pprint as pp

class LogService(ILogService):

    def __init__(self, repo):
        self._repo = repo

    def stack_trace(self, exception):
        stack = traceback.extract_stack()[:-3] + traceback.extract_tb(exception.__traceback__)  # add limit=?? 
        pretty = traceback.format_list(stack)
        return ''.join(pretty) + '\n  {} {}'.format(exception.__class__,exception)

    def log_exception(self, error):
        """build the exception object and log it"""
        try:
            stack_trace = self.stack_trace(error)
            log = dict(exception_log_id=str(uuid.uuid4()),
                   exception_log_type=ExceptionType.SERVICE_EXCEPTION.value,
                   session_id=session['session_id'] if 'session_id' in session else str(uuid.UUID('00000000-0000-0000-0000-000000000000')),
                   occurred_on_utc=datetime.utcnow(),
                   is_handled = True,
                   stack_trace = stack_trace)
            
            self.upsert_exception(log)
            
        except Exception as e:
            print("Service Exception: {}".format(e))


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

    def log_activity(self, error):
        """Build the activity object and log it"""

    def upsert_activity(self, activity_log):
        """insert of update an activity log"""
        self._repo.upsert_activity(activity_log)

    def delete_activity(self, activity_log_id):
        """removes an activity log from the data store"""
        self._repo.delete_activity(activity_log_id)
