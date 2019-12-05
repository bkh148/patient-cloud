import abc

class IInviteRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_invite_by_id(self, invite_id):
        """ return a invite object by it's id. """
        
    @abc.abstractmethod
    def get_all_invites(self):
        """ return all invites in the system """

    @abc.abstractmethod
    def upsert_invite(self, invite):
        """ update or insert a new invite into the table"""

    @abc.abstractmethod
    def delete_invite(self, invite_id):
        """ remove an invite from the table """

    @abc.abstractmethod
    def has_invite(self, invite_id):
        """ evaluate if an invite is in the table """

    @abc.abstractmethod
    def get_invites_created_by(self, user_id):
        """ get all invites created by a user"""

    @abc.abstractmethod
    def get_invites_created_for(self, email):
        """ get all invites created for a user"""
