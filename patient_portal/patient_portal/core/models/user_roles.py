import enum

class UserRole(enum.Enum):
    ADMIN = 'ADMIN'
    LOCAL_ADMIN = 'LOCAL_ADMIN'
    CLINICIAN = 'CLINICIAN'
    PATIENT = 'PATIENT'
