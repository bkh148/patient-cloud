"""Module describing the various IoC Containers needed for the applications injection"""

from dependency_injector import containers, providers
from patient_portal.core import *
from patient_portal.data import *
from patient_portal.config import *
from patient_portal.sqlite import SQLiteDatabase

class DataStores(containers.DeclarativeContainer):

    development_database = providers.Singleton(
        SQLiteDatabase,
        config = DevelopmentConfig()
    )

    production_database = providers.Singleton(
        SQLiteDatabase,
        config = ProductionConfig()
    )

    # 🚨: temp until environments are fixed
    mode = "development"
    database = development_database if mode == 'development' else production_database

class Repositories(containers.DeclarativeContainer):

    appointment_repo = providers.Singleton(
        AppointmentRepository, db=DataStores.database)

    log_repo = providers.Singleton(
        LogRepository, db=DataStores.database
    )

    session_repo = providers.Singleton(
        SessionRepository, db=DataStores.database
    )

    invite_repo = providers.Singleton(
        InviteRepository, db=DataStores.database
    )

    location_repo = providers.Singleton(
        LocationRepository, db=DataStores.database
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
