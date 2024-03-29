from ..interfaces import IInviteService


class InviteService(IInviteService):
    """
    Implementation of the abstract IInviteRepository.
    """

    def __init__(self, repo, log_service):
        self._repo = repo
        self._log_service = log_service

    def get_all_invites(self):
        """ return all invites in the system """
        try:
            return self._repo.get_all_invites()
        except Exception as e:
            self._log_service.log_exception(e)

    def get_invite_by_id(self, invite_id):
        """ return a invite object by it's id. """
        try:
            return self._repo.get_invite_by_id(invite_id)
        except Exception as e:
            self._log_service.log_exception(e)

        return None

    def upsert_invite(self, invite):
        """ update or insert a new invite into the table"""
        try:
            self._repo.upsert_invite(invite)
        except Exception as e:
            self._log_service.log_exception(e)
            raise

    def delete_invite(self, invite_id):
        """ remove an invite from the table """
        try:
            self._repo.delete_invite(invite_id)
        except Exception as e:
            self._log_service.log_exception(e)
            raise

    def get_invites_created_by(self, user_id):
        """ get all invites created by a user"""
        try:
            return self._repo.get_invites_created_by(user_id)
        except Exception as e:
            self._log_service.log_exception(e)

        return []

    def get_invites_created_for(self, email):
        """ get all invites created for a user"""
        try:
            return self._repo.get_invites_created_for(email)
        except Exception as e:
            self._log_service.log_exception(e)

        return []
