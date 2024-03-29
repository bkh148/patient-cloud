from ..interfaces import IUserService
from werkzeug.security import generate_password_hash, check_password_hash


class UserService(IUserService):

    def __init__(self, user_repo, password_service, log_service):
        self._user_repo = user_repo
        self._password_service = password_service
        self._log_service = log_service

    def upsert_user(self, user):
        try:
            self._user_repo.upsert_user(user)
        except Exception as e:
            self._log_service.log_exception(e)
            raise

    def upsert_user_role_map(self, user_role_map):
        """ Create or update a user role map """
        try:
            self._user_repo.upsert_user_role_map(user_role_map)
        except Exception as e:
            self._log_service.log_exception(e)

    def upsert_patient_clinician_map(self, clinician_id, patient_id):
        """ Create a mapping between patient and clinician """
        try:
            self._user_repo.upsert_patient_clinician_map(
                clinician_id, patient_id)
        except Exception as e:
            self._log_service.log_exception(e)

    def get_user_by_id(self, user_id):
        try:
            return self._user_repo.get_user_by_id(user_id)
        except Exception as e:
            self._log_service.log_exception(e)

        return None

    def validate_user(self, user_mail, user_password):
        """ validate a user authentication request """
        try:
            user = self.get_user_by_email(user_mail)

            if user:
                password = self._password_service.get_password_hash(
                    user['user_id'])
                user['role'] = self._user_repo.get_user_role_by_id(user['user_id'])[
                    "user_role"]
                if password and check_password_hash(password['password_hash'], user_password):
                    return user
                else:
                    return None
            else:
                return None
        except Exception as e:
            self._log_service.log_exception(e)

        return None

    def get_user_by_email(self, user_mail):
        """ get a user object by the id """
        try:
            return self._user_repo.get_user_by_email(user_mail)
        except Exception as e:
            self._log_service.log_exception(e)
        return None

    def get_user_role_ids(self, user_roles):
        """ return the ids of user roles """
        try:
            return self._user_repo.get_user_role_ids(user_roles)
        except Exception as e:
            self._log_service.log_exception(e)

        return {}

    def get_user_role(self, user_role_id):
        """ get a user role by it's id """
        try:
            return self._user_repo.get_user_role(user_role_id)
        except Exception as e:
            self._log_service.log_exception(e)

    def get_user_role_by_id(self, user_id):
        """ get a user's role by their id """

    def get_user_role_by_email(self, user_mail):
        """ get a user's role by their email """

    def get_patient_clinician(self, patient_id):
        """return the clinician overlooking this patient's care"""
        try:
            return self._user_repo.get_patient_clinician(patient_id)
        except Exception as e:
            self._log_service.log_exception(e)
            raise

    def get_all_users_patients(self, clinician_id):
        """ get all patients for a clinician """
        try:
            return self._user_repo.get_all_users_patients(clinician_id)
        except Exception as e:
            self._log_service.log_exception(e)

        return None

    def get_all_users_in_location(self, location_id):
        """ get all users in a given location """
