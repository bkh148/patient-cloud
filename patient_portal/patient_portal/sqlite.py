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
            self.create_care_location_table()
            self.create_appointments_table()
            self.create_invite_table()
            self.create_activity_table()
            self.create_activity_type_table()
            self.create_exception_table()
            self.create_exception_type_table()

            print('Database initialiase successfully... 🎉')
        except Exception as e:
            print('An error has occurred whilst setting up the database: {}'.format(e))


    def create_user_table(self):
        print('Create user table')

    def create_user_role_table(self):
        print('Create user role table')

    def create_user_role_map_table(self):
        print('Create user role map')

    def create_password_table(self):
        print('Create password table')

    def create_session_table(self):
        print('Create session table')

    def create_location_table(self):
        print('Create location table')

    def create_care_location_table(self):
        print('Create care location table')

    def create_appointments_table(self):
        print('Create appointments table')

    def create_invite_table(self):
        print('Create invite table')

    def create_activity_table(self):
        print('Create activity table')

    def create_activity_type_table(self):
        print('Create activty type table')

    def create_exception_table(self):
        print('Create exception table')

    def create_exception_type_table(self):
        print('Create exception type table')
