import abc

class IPasswordRepository(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def upsert_password(self, user_id, user_password):
        """ Update or insert a password into the db """

    @abc.abstractmethod
    def has_password(self, user_id):
        """ Check if a password already is in database """
        
    @abc.abstractmethod
    def delete_password(self, user_id):
        """ Delete a password for a given user id """
        
    @abc.abstractmethod
    def get_password_hash(self, user_id):
        """ Return the password has for a given user_id """
