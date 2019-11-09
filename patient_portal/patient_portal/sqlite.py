import sqlite3
from pprint import pprint as pp

class SQLiteDatabase(object):

    def __init__(self, config):
        self._config = config


    def connection(self):
        try:
            return sqlite3.connect(self._config.DATABASE_URI)
        except Exception as e:
            print('Connection issue: {}'.format(e))
            raise e

    def initialise_database(self):
        """Initialise the databse"""
        try:

            self.create_user_table()
            self.create_user_role_table()
            self.create_user_role_map_table()
            self.create_password_table()
            self.create_session_table()
            self.create_location_table()
            self.create_appointments_table()
            self.create_invite_table()
            self.create_activity_table()
            self.create_exception_table()

            print('{} initialised successfully... 🎉'.format(self._config.MODE))
        except Exception as e:
            print('An error has occurred whilst setting up the database: {}'.format(e))


    def create_user_table(self):
        print('Create user table')
        self.connection().execute("""
        CREATE TABLE IF NOT EXISTS user(
        user_id TEXT PRIMARY KEY NOT NULL,
        user_role_map_id TEXT NOT NULL,
        user_email TEXT NOT NULL,
        user_forname TEXT NOT NULL,
        user_lastname TEXT NOT NULL,
        CONSTRAINT unique_email UNIQUE (user_email),
        FOREIGN KEY (user_role_map_id) REFERENCES user_role_map(user_role_map_id))
        """)

    def create_user_role_table(self):
        print('Create user role table')
        self.connection().execute("""
        CREATE TABLE IF NOT EXISTS user_role (
        user_role_id TEXT PRIMARY KEY NOT NULL,
        user_role TEXT NOT NULL,
        CONSTRAINT unique_user_role_id UNIQUE (user_role_id),
        CONSTRAINT unique_user_role UNIQUE (user_role))
        """)

    def create_user_role_map_table(self):
        print('Create user role map')
        self.connection().execute("""
        CREATE TABLE IF NOT EXISTS user_role_map (
        user_role_map_id TEXT PRIMARY KEY NOT NULL,
        user_role_id TEXT NOT NULL,
        location_id TEXT NOT NULL,
        FOREIGN KEY (user_role_id) REFERENCES user_role(user_role_id),
        FOREIGN KEY (location_id) REFERENCES location(location_id))
        """)

    def create_password_table(self):
        print('Create password table')
        self.connection().execute("""
        CREATE TABLE IF NOT EXISTS passwords(
        password_id TEXT PRIMARY KEY NOT NULL,
        user_id TEXT NOT NULL,
        password_hash TEXt NOT NULL,
        CONSTRAINT unique_password_id UNIQUE (password_id),
        CONSTRAINT unique_user_id UNIQUE (user_id),
        FOREIGN KEY (user_id) REFERENCES user(user_id))
        """)

    def create_session_table(self):
        print('Create session table')
        self.connection().execute("""
        CREATE TABLE IF NOT EXISTS session(
        session_id TEXT PRIMARY KEY NOT NULL,
        user_id TEXT NOT NULL,
        session_last_active_date_utc TEXT NOT NULL,
        metadata TEXT NOT NULL,
        CONSTRAINT unique_session_user_id UNIQUE (user_id),
        FOREIGN KEY (user_id) REFERENCES user(user_id))
        """)

    def create_location_table(self):
        print('Create location table')
        self.connection().execute("""
        CREATE TABLE IF NOT EXISTS location(
        location_id TEXT PRIMARY KEY NOT NULL,
        location_name TEXT NOT NULL,
        location_coord_x REAL NOT NULL,
        location_coord_y REAL NOT NULL,
        location_postcode TEXT NOT NULL,
        location_address TEXT NOT NULL,
        CONSTRAINT unique_location_id UNIQUE (location_id))
        """)

    # TODO: Relations + constraints
    def create_appointments_table(self):
        print('Create appointments table')
        self.connection().execute("""
        CREATE TABLE IF NOT EXISTS appointments(
        appointment_id TEXT PRIMARY KEY NOt NULL,
        created_by TEXT NOT NULL,
        created_for TEXT NOT NULL,
        location_id TEXT NOT NULL,
        created_on_utc TEXT NOT NULL,
        appointment_date_utc TEXT NOT NULL,
        appointment_type TEXT NOT NULL,
        appointment_notes TEXT,
        is_cancelled BIT DEFAULT 0,
        is_attended BIT DEFAULT 0,
        CONSTRAINT unique_appointment_id UNIQUE (appointment_id),
        FOREIGN KEY (created_by) REFERENCES user(user_id),
        FOREIGN KEY (created_for) REFERENCES appointment(user_id),
        FOREIGN KEY (location_id) REFERENCES location(location_id))
        """)

    def create_invite_table(self):
        print('Create invite table')
        self.connection().execute("""
        CREATE TABLE IF NOT EXISTS invite(
        invite_id TEXT PRIMARY KEY NOT NULL,
        invited_by TEXT NOT NULL,
        user_role_id TEXT NOT NULL,
        invited_email TEXT NOT NULL,
        invited_on_utc TEXT NOT NULL,
        expiration_date_utc TEXT NOT NULL,
        is_consumed TEXT DEFAULT 0,
        CONSTRAINT unique_invite_id UNIQUE (invite_id),
        FOREIGN KEY (invited_by) REFERENCES users(user_id),
        FOREIGN KEY (user_role_id) REFERENCES user_role(user_role_id))
        """)

    def create_activity_table(self):
        print('Create activity table')
        self.connection().execute("""
        CREATE TABLE IF NOT EXISTS activity_log(
        activity_log_id TEXT PRIMARY KEY NOT NULL,
        activity_log_type TEXT NOT NULL,
        session_id TEXT NOT NULL,
        occurred_on_utc TEXT NOT NULL,
        CONSTRAINT unique_activity_log_id UNIQUE (activity_log_id),
        FOREIGN KEY (session_id) REFERENCES session(session_id))
        """)

    def create_exception_table(self):
        print('Create exception table')
        self.connection().execute("""
        CREATE TABLE IF NOT EXISTS exception_log(
        exception_log_id TEXT PRIMARY KEY NOT NULL,
        exception_log_type TEXT NOT NULL,
        session_id TEXT NOT NULL,
        occurred_on_utc TEXT NOT NULL,
        is_handled BIT DEFAULT 0,
        stack_trace TEXT NOT NULL,
        CONSTRAINT unique_exception_log_id UNIQUE (exception_log_id),
        FOREIGN KEY (session_id) REFERENCES session(session_id))
        """)
