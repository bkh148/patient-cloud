import abc

class IUserRepository(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def upsert_user(self, user):
        """ Create or update a user model """
        
    @abc.abstractmethod
    def has_user(self, user_id):
        """ Evaluate if a user exists in datastore """
    
    @abc.abstractmethod
    def get_user_by_id(self, user_id):
        """ get a user object by the the user id """
    
    @abc.abstractmethod
    def get_user_by_email(self, user_mail):
        """ get a user object by the id """

    @abc.abstractmethod
    def get_user_role_ids(self, user_roles):
        """ return the ids of user roles """
    
    @abc.abstractmethod
    def get_user_role(self, user_role_id):
        """ get a user role by it's id"""
    
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
    def get_patient_clinician(self, patient_id): 
        """return the clinician overlooking this patient's care"""    
        
    @abc.abstractmethod
    def get_all_users_in_location(self, location_id):
        """ get all users in a given location """
