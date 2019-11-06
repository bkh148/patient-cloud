"""Module responsible for starting up the web application"""

from flask import render_template
from patient_portal import initialise_application

from start_up import app, socket_io

if __name__ == '__main__':
    socket_io.run(app, log_output=True)
