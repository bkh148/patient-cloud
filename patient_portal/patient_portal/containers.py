"""Module describing the various IoC Containers needed for the applications injection"""

from dependency_injector import containers, providers
from patient_portal.core import *
from patient_portal.data import *

class Repositories(containers.DeclarativeContainer):

    appointment_repo = providers.Singleton(
        AppointmentRepository, connection=dict(uid='2354', message='Hello, world!'))

    log_repo = providers.Singleton(
        LogRepository, connection=dict(uid='2345', message='Hello, world!')
    )

    session_repo = providers.Singleton(
        SessionRepository, connection=dict()
    )

    invite_repo = providers.Singleton(
        InviteRepository, connection=dict()
    )

    location_repo = providers.Singleton(
        LocationRepository, connection=dict()
    )

class Services(containers.DeclarativeContainer):

    appointment_service = providers.Singleton(
        AppointmentService,
        repo=Repositories.appointment_repo
    )

    log_service = providers.Singleton(
        LogService,
        repo=Repositories.log_repo
    )

    session_service = providers.Singleton(
        SessionService,
        repo=Repositories.session_repo
    )

    invite_service = providers.Singleton(
        InviteService,
        repo=Repositories.invite_repo
    )

    location_service = providers.Singleton(
        LocationService,
        repo=Repositories.location_repo
    )
