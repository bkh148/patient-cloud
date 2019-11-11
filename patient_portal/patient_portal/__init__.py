"""Module responsible for setting up app defintion rules"""
import eventlet
eventlet.monkey_patch()

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_socketio import SocketIO
from flask_moment import Moment
from patient_portal.containers import Services, DataStores
from patient_portal.sqlite import SQLiteDatabase

services = Services()
socket_io = SocketIO()
toolbar = DebugToolbarExtension()
moment = Moment()

def initialise_application(configuration):
    """Create an instance of the flask application
    Args:
        configuration: A configuration object for settings various server settings.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'

    # if debug / prod /test
    database = DataStores.database()
    database.initialise_database()

    toolbar.init_app(app)
    moment.init_app(app)

    from .auth import auth as auth_blueprint
    from .admin import admin as admin_blueprint
    from .local_admin import local_admin as local_admin_blueprint
    from .clinician import clinician as clinician_blueprint
    from .patient import patient as patient_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    app.register_blueprint(local_admin_blueprint, url_prefix="/local_admin")
    app.register_blueprint(clinician_blueprint, url_prefix='/clinician')
    app.register_blueprint(patient_blueprint, url_prefix='/patient')

    socket_io.init_app(app, logger=True, engineio_logger=True)

    return app, socket_io
