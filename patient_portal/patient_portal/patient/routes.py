"""Module for handling normal user routes"""

from . import patient
from flask import render_template

@patient.route('/', methods=['GET'])
@patient.route('/dashboard', methods=['GET'])
def dashboard():
    """Handle the patient dashboard"""

    socket_config = {
        "host": "127.0.0.1",
        "port": "5000",
        "namespace": "patient"}

    dashboard = {
        "text": "Dashboard",
        "style": "active",
        "url": "",
        "icon": "fas fa-home"}

    appointments = {
        "text": "Appointments",
        "style": "",
        "url": "",
        "icon": "fas fa-calendar-check"}

    return render_template('patient/index.html', title='Dashboard - Patient',
                           static_folder='patient.static',
                           style_paths=['css/main.css'],
                           nav_links=[dashboard, appointments],
                           configurations=socket_config)
