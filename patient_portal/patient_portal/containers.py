"""Module describing the various IoC Containers needed for the applications injection"""

from dependency_injector import containers, providers
from patient_portal.core import AppointmentService
from patient_portal.data import AppointmentRepository

class Repositories(containers.DeclarativeContainer):

    appointment_repo = providers.Singleton(
        AppointmentRepository, connection=dict(uid='2354', message='Hello, worl!'))


class Services(containers.DeclarativeContainer):

    appointment_service = providers.Singleton(
        AppointmentService,
        repo=Repositories.appointment_repo
    )



