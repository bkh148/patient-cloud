from ..interfaces import IUserRepository

class UserRepository(IUserRepository):
    
    def __init__(self, db):
        self._db = db
    
    def get_user_by_id(self, user_id):
        """ get a user object by the the user id """
        return db.execute("SELECT * FROM user;")
    
    def get_all_users_patients(self, clinician_id):
        """ get all patients for a clinician """
        connection = self._db.connection()
        return connection.execute("""
        SELECT user_id, user_email, user_forname, user_lastname FROM user t1
        LEFT JOIN patient_clinician_map t2 ON t1.user_id = t2.patient_id
        WHERE clinician_id = ?""", (clinician_id, )).fetchall()

    def get_user_by_email(self, user_mail):
        """ get a user object by the id """
    
    def get_user_role_by_id(self, user_id):
        """ get a user's role by their id """
    
    def get_user_role_by_email(self, user_mail):
        """ get a user's role by their email """
        
    def get_all_users_in_location(self, location_id):
        """ get all users in a given location """
