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
    
    user_repo = providers.Singleton(
        UserRepository, db=DataStores.database
    )
    
    password_repo = providers.Singleton(
        PasswordRepository, db=DataStores.database
    )

class Services(containers.DeclarativeContainer):

    config = providers.Configuration('config')
    mail_server = config.mail_server

    log_service = providers.Singleton(
        LogService,
        repo=Repositories.log_repo
    )

    appointment_service = providers.Singleton(
        AppointmentService,
        repo=Repositories.appointment_repo,
        log_service=log_service
    )

    session_service = providers.Singleton(
        SessionService,
        repo=Repositories.session_repo,
        log_service=log_service
    )

    password_service = providers.Singleton(
        PasswordService,
        repo=Repositories.password_repo,
        log_service = log_service
    )

    invite_service = providers.Singleton(
        InviteService,
        repo=Repositories.invite_repo,
        log_service=log_service
    )

    location_service = providers.Singleton(
        LocationService,
        loc_repo=Repositories.location_repo,
        log_service=log_service
    )
    
    user_service = providers.Singleton(
        UserService,
        user_repo=Repositories.user_repo,
        password_service=password_service,
        log_service=log_service
    )
    
    email_service = providers.Singleton(
        EmailService,
        mail_server = mail_server,
        invite_repo = Repositories.invite_repo,
        user_service = user_service,
        log_service = log_service
    )
