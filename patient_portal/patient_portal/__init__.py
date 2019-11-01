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
    from .local_admin import local_admin as local_admin_blueprint
    from .clinician import clinician as clinician_blueprint
    from .patient import patient as patient_blueprint

    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    app.register_blueprint(local_admin_blueprint, url_prefix="/local_admin")
    app.register_blueprint(clinician_blueprint, url_prefix='/clinician')
    app.register_blueprint(patient_blueprint, url_prefix='/patient')

    return app
