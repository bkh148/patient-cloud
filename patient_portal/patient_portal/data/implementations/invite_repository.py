
from ..interfaces import IInviteRepository


class InviteRepository(IInviteRepository):

    def __init__(self, db):
        self._db = db

    def get_invite_by_id(self, invite_id):
        """ return a invite object by it's id. """
        return self._db.get_single("""
        SELECT * FROM invite 
        WHERE invite_id = ?""", (invite_id,))

    def get_all_invites(self):
        """ return all invites in the system """
        return self._db._get_all("""
        SELECT * FROM invite""")

    def upsert_invite(self, invite):
        """ update or insert a new invite into the table"""

        if self.has_invite(invite['invite_id']):
            self._db.update('invite', invite)
        else:
            self._db.insert('invite', invite)

    def delete_invite(self, invite_id):
        """ remove an invite from the table """
        self._db.execute("""
        DELETE FROM invite
        WHERE invite_id = ?""", (invite_id, ))

    def has_invite(self, invite_id):
        """ evaluate if an invite is in the table """
        return self._db.count("""
        SELECT COUNT() FROM invite
        WHERE invite_id = ? """, (invite_id, )) > 0

    def get_invites_created_by(self, user_id):
        """ get all invites created by a user"""
        return self._db.get_all("""
        SELECT * FROM invite
        WHERE invited_by = ?""", (user_id, ))

    def get_invites_created_for(self, email):
        """ get all invites created for a user"""
        return self._db.get_all("""
        SELECT * FROM invite
        WHERE invited_email = ?""", (email, ))
