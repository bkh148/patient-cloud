"""Module responsible for setting up app defintion rules"""
from patient_portal.config import *
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from patient_portal.containers import *
from flask_socketio import SocketIO
from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask
import eventlet
import os


# Monkey patch socket as suggested: https://github.com/miguelgrinberg/python-engineio/issues/19
eventlet.monkey_patch(socket=True)

app = Flask(__name__)
app.config.from_object(DevelopmentConfig() if os.getenv(
    'FLASK_ENV', 'development') == 'development' else ProductionConfig())

jwt_manager = JWTManager()
socket_io = SocketIO()
mail = Mail()

# register configurations in the configs IoC
configs = Configs.config.override(app.config)

# register mail server in the services IoC
services = Services(config={'mail_server': mail})


# HACK: This is a temporary solution. The application will need to know what users are online 
# for various socket operations. This should eventually be moved into it's own module with various abstraction methods due to code repetition
online_patients = {}
online_clinicians = {}
online_admins = {}
online_local_admins = {}


def initialise_application():
    """Create an instance of the flask application
    Args:
        configuration: A configuration object for settings various server settings.
    """

    # Initialise the flask mail plugin
    mail = Mail(app)

    # Initialise the JWT Token plugin
    jwt_manager = JWTManager(app)

    # Initialise the data store
    DataStores.database().initialise_database()

    # This will be skipped in production
    toolbar = DebugToolbarExtension()
    toolbar.init_app(app)

    from .auth import auth as auth_blueprint
    from .admin import admin as admin_blueprint
    from .local_admin import local_admin as local_admin_blueprint
    from .clinician import clinician as clinician_blueprint
    from .patient import patient as patient_blueprint
    from .api_v1 import api_v1 as api_v1_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    app.register_blueprint(local_admin_blueprint, url_prefix="/local_admin")
    app.register_blueprint(clinician_blueprint, url_prefix='/clinician')
    app.register_blueprint(patient_blueprint, url_prefix='/patient')
    app.register_blueprint(api_v1_blueprint)

    socket_io.init_app(app, logger=True)

    return app, socket_io
