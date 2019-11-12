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

    # Get the following from the session when authentication is setup
    metadata['settings'] = {}
    metadata['configurations'] = {}
    metadata['carelocation'] = {}
    metadata['settings'] = {
        "care_location": "8cb58fa5-1a6c-484b-ac9a-98cadb53064b",
        "forename": "Liam",
        "surname": "Lamb",
        "email": "liam.j.lamb@gmail.com",
        "active_account": 1,
        "stay_logged_in": 1}

    try:
        appointments = services.appointment_service().get_appointments_for('0f837187-be84-4c4d-a3b6-745598174959')
        metadata['appointments']['upcoming'] = appointments
        metadata['components'] = ['appointments', 'settings']
        # Get from session
        metadata['carelocation'] = services.location_service().get_location_by_id('8cb58fa5-1a6c-484b-ac9a-98cadb53064b')
        metadata['configurations'] = {
        "host": "127.0.0.1",
        "port": "5000",
        "namespace": "patient"}

    except Exception as e:
        # Log error
        print("Some exception.. {}", e)

    appointments = {
        "text": "Appointments",
        "style": "active",
        "context": metadata['components'][0],
        "icon": "fas fa-calendar-check"}

    return render_template('patient/index.html', title='Dashboard - Patient',
                           static_folder='patient.static',
                           style_paths=['css/main.css'],
                           nav_links=[appointments],
                           metadata=metadata)
