"""Module responsible for setting up app defintion rules"""

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension()

def initialise_application(configuration):
    """Create an instance of the flask application
    Args:
        configuration: A configuration object for settings various server settings.
    """
    app = Flask(__name__)
    toolbar.init_app(app)

    from .nav import admin_blueprint, auth_blueprint, nuser_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(nuser_blueprint, url_prefix='/user')

    return app
