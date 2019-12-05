from .appointments import nsp as appointment_nsp
from .locations import nsp as location_nsp
from .invites import nsp as invitation_nsp
from .logs import nsp as log_nsp

__all__ = ['location_nsp', 'appointment_nsp', 'invitation_nsp', 'log_nsp']
