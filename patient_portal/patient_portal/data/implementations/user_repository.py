from ..interfaces import IUserRepository


class UserRepository(IUserRepository):

    def __init__(self, db):
        self._db = db

    def upsert_user(self, user):
        """ Create or update a user model """
        if self.has_user(user['user_id']):
            self._db.update('user', user)
        else:
            self._db.insert('user', user)

    def has_user(self, user_id):
        """ Evaluate if a user exists in datastore """
        return self._db.count("""
            SELECT COUNT() FROM user
            WHERE user_id = ?""", (user_id, )) > 0

    def get_user_by_id(self, user_id):
        """ get a user object by the the user id """
        return self._db.get_single("""
        SELECT * FROM user
        WHERE user_id = ?""", (user_id, ))

    def get_all_users_patients(self, clinician_id):
        """ get all patients for a clinician """
        return self._db.get_all("""
        SELECT user_id, user_email, user_forname, user_lastname FROM user t1
        LEFT JOIN patient_clinician_map t2 ON t1.user_id = t2.patient_id
        WHERE clinician_id = ?""", (clinician_id, ))

    def get_user_by_email(self, user_mail):
        """ get a user object by the id """
        return self._db.get_single("""
        SELECT * FROM user WHERE user_email = ?""", (user_mail, ))

    def get_user_role(self, user_role_id):
        """ get a user role by it's id """
        return self._db.get_single("""
        SELECT user_role FROM user_role
        WHERE user_role_id = ?""", (user_role_id, ))

    def get_user_role_by_id(self, user_id):
        """ get a user's role by their id """
        return self._db.get_single("""
        SELECT user_role FROM user t1
        LEFT JOIN user_role_map t2 ON t1.user_role_map_id = t2.user_role_map_id
        LEFT JOIN user_role t3 ON t2.user_role_id = t3.user_role_id
        WHERE user_id = ?""", (user_id, ))

    def get_user_role_ids(self, user_roles):
        """ return the ids of user roles """

        query = """
        SELECT * FROM user_role
        WHERE user_role IN ({})""".format(','.join('?' * len(user_roles)))

        result = self._db.get_all(query, user_roles)
        return {item['user_role']: item['user_role_id'] for item in result}

    def get_user_role_by_email(self, user_mail):
        """ get a user's role by their email """

    def get_patient_clinician(self, patient_id):
        """return the clinician overlooking this patient's care"""
        return self._db.get_single("""
        SELECT user_id, user_email, user_forname, user_lastname FROM user t1
        LEFT JOIN patient_clinician_map t2 ON t1.user_id = t2.clinician_id
        WHERE patient_id = ?""", (patient_id, ))

    def get_all_users_in_location(self, location_id):
        """ get all users in a given location """
