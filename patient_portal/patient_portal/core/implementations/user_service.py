from ..interfaces import IUserService
from werkzeug.security import generate_password_hash, check_password_hash

class UserService(IUserService):
    
    def __init__(self, user_repo, password_service, log_service):
        self._user_repo = user_repo
        self._password_service = password_service
        self._log_service = log_service
        
    def get_user_by_id(self, user_id):
        try :
            # TODO: log service call
            return self._user_repo.get_user_by_id(user_id);
        except Exception as e:
            # TODO: logging
            print("Service Exception {} : {}".format(__name__, e))
        
        return None;
    
    def validate_user(self, user_mail, user_password):
        """ validate a user authentication request """ 
        try:
            user = self.get_user_by_email(user_mail)
        
            if user:
                password = self._password_service.get_password_hash(user['user_id'])
                user['role'] = self._user_repo.get_user_role_by_id(user['user_id'])["user_role"]
                if password and check_password_hash(password['password_hash'], user_password):
                    return user
                else:
                    return None
            else:
                return None
        except Exception as e:
            print("Service Exception {} : {}".format(__name__, e))
            
        return None
            
    
    def get_user_by_email(self, user_mail):
        """ get a user object by the id """
        try :
            return self._user_repo.get_user_by_email(user_mail)
        except Exception as e:
            print("Service Exception {}: {}".format(__name__, e))
        return None;
    
    def get_user_role_by_id(self, user_id):
        """ get a user's role by their id """
    
    def get_user_role_by_email(self, user_mail):
        """ get a user's role by their email """
    
    def get_patient_clinician(self, patient_id): 
        """return the clinician overlooking this patient's care"""
        try:
            #Todo: log activity
            return self._user_repo.get_patient_clinician(patient_id)
        except Exception as e:
            #Todo: log exception
            print("Service Exception {} : {}".format(__name__, e))
            
    
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
