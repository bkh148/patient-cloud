from ..interfaces import IPasswordService

class PasswordService(IPasswordService):
    
    def __init__(self, repo, log_service):
        self._repo = repo
        self._log_service = log_service
    
    def upsert_password(self, user_id, user_password):
        """ Update or insert a password into the db """
        try:
            self._repo.upsert_password(user_id, user_password)
        except Exception as e:
            self._log_service.log_exception(e)
            raise
        
    def delete_password(self, user_id):
        """ Delete a password for a given user id """
        try:
            self._repo.delete_password(user_id)
        except Exception as e:
            self._log_service.log_exception(e)
            raise
        
    def get_password_hash(self, user_id):
        """ Return the password has for a given user_id """
        try:
            return self._repo.get_password_hash(user_id)
        except Exception as e:
            self._log_service.log_exception(e)
        return None
