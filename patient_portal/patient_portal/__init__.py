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

    from .admin import admin as admin_blueprint
    from .auth import auth as auth_blueprint
    from .nuser import nuser as nuser_blueprint

    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(nuser_blueprint, url_prefix='/user')

    return app
