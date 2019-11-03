"""Module responsible for starting up the web application"""

from flask import render_template
from patient_portal import initialise_application

from start_up import app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
