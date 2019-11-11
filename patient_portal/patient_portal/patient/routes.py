"""Module for handling normal user routes"""

from . import patient
from flask import render_template

from .. import services

@patient.route('/', methods=['GET'])
@patient.route('/dashboard', methods=['GET'])
def dashboard():
    """Handle the patient dashboard"""

    metadata = {}
    metadata['appointments'] = {}

    try:
        appointments = services.appointment_service().get_appointments_for('0f837187-be84-4c4d-a3b6-745598174959')
        metadata['appointments']['upcoming'] = appointments

        print(metadata)

    except Exception as e:
        print("Some exception..")
        raise e

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
                           configurations=socket_config,
                           metadata=metadata)
