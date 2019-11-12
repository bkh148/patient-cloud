from ..interfaces import IUserService

class UserService(IUserService):
    
    def __init__(self, user_repo, log_service):
        self._user_repo = user_repo
        self._log_service = log_service
        
    def get_user_by_id(self, user_id):
        try :
            # TODO: log service call
            return self._user_repo.get_user_by_id(user_id);
        except Exception as e:
            # TODO: logging
            print("Service Exception {} : {}".format(__name__, e))
        
        return None;
            
    
    def get_user_by_email(self, user_mail):
        """ get a user object by the id """
    
    def get_user_role_by_id(self, user_id):
        """ get a user's role by their id """
    
    def get_user_role_by_email(self, user_mail):
        """ get a user's role by their email """
        
    def get_all_users_patients(self, clinician_id):
        """ get all patients for a clinician """
        try :
            #TODO: log service call
            return self._user_repo.get_all_users_patients(clinician_id);
        except Exception as e:
            #TODO: log exception
            print("Service Exception {} : {}".format(__name__, e))
        
        return None;
    def get_all_users_in_location(self, location_id):
        """ get all users in a given location """
