"""Module for handling the clinician's content in the applciation"""

from . import clinician
from flask import render_template

@clinician.route('/', methods=['GET'])
@clinician.route('/dashboard', methods=['GET'])
def dashboard():
    """Handle the clincian dashboard"""

    socket_config = {
        "host": "127.0.0.1",
        "port": "5000",
        "namespace": "clinician"}

    dashboard = {
        "text": "Dashboard",
        "style": "active",
        "url": "",
        "icon": "fas fa-home"}

    patients = {
        "text": "Patients",
        "style": "",
        "url": "",
        "icon": "fas fa-procedures"}

    appointments = {
        "text": "Appointments",
        "style": "",
        "url": "",
        "icon": "fas fa-calendar-check"}

    return render_template('clinician/index.html', title='Dashboard - Clinician',
                           static_folder='clinician.static',
                           style_paths=['css/main.css'],
                           nav_links=[dashboard, patients, appointments],
                           configurations=socket_config)
