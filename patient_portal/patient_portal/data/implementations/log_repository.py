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
        return self._db.get_all("""
            SELECT * FROM exception_log
            WHERE session_id = ?""", (session_id, ))


    def upsert_exception(self, exception_log):
        """inserts or updates an exception log

        Args:
            exception_log: a full log object to either insert or update appropriately.

        """
        if self.has_exception(exception_log["exception_log_id"]):
            self._db.update('exception_log', exception_log)
        else:
            self._db.insert('exception_log', exception_log)

    def has_exception(self, exception_log_id):
        """evaluates if an exception log is in the data store"""
        return self._db.count("""
            SELECT COUNT() FROM exception_log
            WHERE exception_log_id = ?""", (exception_log_id, )) > 0
        

    def delete_exception(self, exception_log_id):
        """removes an exception log from the data store"""
        self._db.execute("""
            DELETE FROM exception_log
            WHERE exception_log_id = ?""", (exception_log_id, ))

    def get_activities_by_session_id(self, session_id):
        """get all activities from a given user session

        Args:
            session_id: user session to retrieve activities for.

        Returns:
            empty [] or [] of activities.
        """
        return self._db.get_all("""
            SELECT * FROM activity_log
            WHERE session_id = ?""", (session_id, ))

    def upsert_activity(self, activity_log):
        """insert of update an activity log"""
        if self.has_activity(activity_log["activity_log_id"]):
            self._db.update('activity_log', activity_log)
        else:
            self._db.insert('activity_log', activity_log)

    def has_activity(self, activity_log_id):
        """evaluates if an activity log is in the data store"""
        return self._db.count("""
            SELECT COUNT() FROM activity_log
            WHERE activity_log_id = ?""", (activity_log_id, )) > 0

    def delete_activity(self, activity_log_id):
        """removes an activity log from the data store"""
        self._db.execute("""
            DELETE FROM exception_log
            WHERE activity_log = ?""", (activity_log_id, ))
