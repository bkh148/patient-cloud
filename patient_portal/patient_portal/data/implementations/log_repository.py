from ..interfaces import ILogRepository

class LogRepository(ILogRepository):

    def __init__(self, db):
        self._db = db

    def get_exceptions_by_session_id(self, session_id):
        """get all exceptions from a given user session

        Args:
            session_id: user session to retrieve exceptions for.

        Returns:
            empty [] or [] of exceptions.
        """
        # SQL Query
        return []


    def upsert_exception(self, exception_log):
        """inserts or updates an exception log

        Args:
            exception_log: a full log object to either insert or update appropriately.

        """

        has_log = self.has_exception(exception_log["exception_log_id"])
        if has_log:
            print('has log')
            # Update query
        else:
            print('doesn\'t have log')
            # Insert query

    def has_exception(self, exception_log_id):
        """evaluates if an exception log is in the data store
        """
        # scalar query to evaluate presence of log.

    def delete_exception(self, exception_log_id):
        """removes an exception log from the data store"""
        # query to delete a lof from exception table

    def get_activities_by_session_id(self, session_id):
        """get all activities from a given user session

        Args:
            session_id: user session to retrieve activities for.

        Returns:
            empty [] or [] of activities.
        """
        # SQL Query
        return []       #

    def upsert_activity(self, activity_log):
        """insert of update an activity log"""

        has_activity = self.has_activity(activity_log["activity_log_id"])

        if has_activity:
            print('has')
            # update a log
        else:
            print('hasn\'t')
            # insert a log

    def has_activity(self, activity_log_id):
        """evaluates if an activity log is in the data store"""
        #scalar to assess if log is in the activity table


    def delete_activity(self, activity_log_id):
        """removes an activity log from the data store"""
        #query to remove the log by id
