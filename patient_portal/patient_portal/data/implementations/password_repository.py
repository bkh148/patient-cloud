from ..interfaces import IPasswordRepository

class PasswordRepository(IPasswordRepository):
    
    def __init__(self, db):
        self._db = db
        
    def upsert_password(self, user_id, user_password):
        """ Update or insert a password into the db """

    def delete_password(self, user_id):
        """ Delete a password for a given user id """
        
    def get_password_hash(self, user_id):
        """ Return the password has for a given user_id """
        return self._db.get_single("""
            SELECT password_hash FROM passwords
            WHERE user_id = ?""", (user_id, ))
