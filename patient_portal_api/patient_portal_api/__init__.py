"""Module responsible for setting up the REST api server"""

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_uuid import FlaskUUID

toolbar = DebugToolbarExtension()
flask_uuid = FlaskUUID()

def initialise_rest_server(configuration):
    """Creates a new instance of the Patient Portal REST API Server
    Args:
        configuration: A configuration object for settings various server settings.
    """

    app = Flask(__name__)

    flask_uuid.init_app(app)
    toolbar.init_app(app)

    from .appointments import appointments as appointments_blueprint
    from .auth import auth as auth_blueprint
    from .care_location import carelocations as carelocation_blueprint
    from .invite import invites as invite_blueprint
    from .location import locations as location_blueprint
    from .log import logs as log_blueprint
    from .session import sessions as session_blueprint
    from .user import users as user_blueprint

    app.register_blueprint(appointments_blueprint, url_prefix='/appointments')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(carelocation_blueprint, url_prefix='/carelocations')
    app.register_blueprint(invite_blueprint, url_prefix='/invites')
    app.register_blueprint(location_blueprint, url_prefix='/locations')
    app.register_blueprint(log_blueprint, url_prefix='/logs')
    app.register_blueprint(session_blueprint, url_prefix='/sessions')
    app.register_blueprint(user_blueprint ,url_prefix='/users')

    return app
