from ..interfaces import IPasswordRepository
import uuid


class PasswordRepository(IPasswordRepository):

    def __init__(self, db):
        self._db = db

    def upsert_password(self, user_id, password_hash):
        """ Update or insert a password into the db """
        if self.has_password(user_id):
            self._db.update('passwords', dict(
                user_id=user_id, password_hash=password_hash))
        else:
            self._db.insert('passwords', dict(password_id=uuid.uuid4(),
                                              user_id=user_id,
                                              password_hash=password_hash))

    def has_password(self, user_id):
        """ Check if a password already is in database """
        return self._db.count("""
            SELECT COUNT() FROM passwords
            WHERE user_id = ?""", (user_id, ))

    def delete_password(self, user_id):
        """ Delete a password for a given user id """
        self._db.execute("""
            DELETE FROM passwords
            WHERE user_id = ?""", (user_id, ))

    def get_password_hash(self, user_id):
        """ Return the password has for a given user_id """
        return self._db.get_single("""
            SELECT password_hash FROM passwords
            WHERE user_id = ?""", (user_id, ))
