from ..interfaces import IInviteService
import abc

class InviteService(IInviteService):
    """
    Implementation of the abstract IInviteRepository.

    Todo: add service call logging
    """
    def __init__(self, repo):
        self._repo = repo

    def upsert_invite(self, invite):
        """ update or insert a new invite into the table"""
        self._repo.upsert_invite(invite)

    def delete_invite(self, invite_id):
        """ remove an invite from the table """
        self._repo.delete_invite(invite_id)

    def get_invites_created_by(self, user_id):
        """ get all invites created by a user"""
        return self._repo.get_invites_created_by(user_id)

    def get_invites_created_for(self, email):
        """ get all invites created for a user"""
        return self._repo.get_invites_created_for(email)
