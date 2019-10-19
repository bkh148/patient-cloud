"""Module responsible for setting up the REST api server"""

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension()

def initialise_rest_server(configuration):
    """Creates a new instance of the Patient Portal REST API Server
    Args:
        configuration: A configuration object for settings various server settings.
    """

    app = Flask(__name__)
    toolbar.init_app(app)

    from .appointments import appointments as appointments_blueprint
    from .auth import auth as auth_blueprint
    from .reports import reports as reports_blueprint

    app.register_blueprint(appointments_blueprint, url_prefix='/appointments')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(reports_blueprint, url_prefix='/reports')

    return app
