
from ..interfaces import IInviteRepository

class InviteRepository(IInviteRepository):

    def __init__(self, db):
        self._db = db

    def upsert_invite(self, invite):
        """ update or insert a new invite into the table"""

    def delete_invite(self, invite_id):
        """ remove an invite from the table """

    def has_invite(self, invite_id):
        """ evaluate if an invite is in the table """

    def get_invites_created_by(self, user_id):
        """ get all invites created by a user"""

    def get_invites_created_for(self, email):
        """ get all invites created for a user"""
