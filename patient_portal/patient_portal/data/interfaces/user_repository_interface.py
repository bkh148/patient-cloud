import abc

class IUserRepository(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def get_user_by_id(self, user_id):
        """ get a user object by the the user id """
    
    @abc.abstractmethod
    def get_user_by_email(self, user_mail):
        """ get a user object by the id """
    
    @abc.abstractmethod
    def get_user_role_by_id(self, user_id):
        """ get a user's role by their id """
    
    @abc.abstractmethod
    def get_user_role_by_email(self, user_mail):
        """ get a user's role by their email """
        
    @abc.abstractmethod
    def get_all_users_patients(self, clinician_id):
        """ get all patients for a clinician """
        
    @abc.abstractmethod
    def get_all_users_in_location(self, location_id):
        """ get all users in a given location """
