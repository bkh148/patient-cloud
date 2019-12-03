"""Module for handling normal user routes"""

from . import patient
from flask import render_template, session
from .. import services
from ..core import login_required

@patient.route('/', methods=['GET'])
@patient.route('/dashboard', methods=['GET'])
@login_required('PATIENT')
def dashboard():
    """Handle the patient dashboard"""

    metadata = {
        'appointments': {},
        'configurations': {},
        'templates': {},
        'components': ['appointments', 'settings'],
        'settings': {},
        'online_users': {}
    }

    try:
        metadata['appointments'] = services.appointment_service().get_appointments_for(session['user']['user_id'])
        session['clinician'] = services.user_service().get_patient_clinician(session['user']['user_id'])
        metadata['locations'] = services.location_service().get_all_locations()
        
        # Get from session
        metadata['configurations'] = {
        "host": "127.0.0.1",
        "port": "5000",
        "namespace": "patient",
        "session_id": session['session_id']}
        
        # Get the following from the session when authentication is setup
        metadata['settings'] = {
            'user': session['user'],
            'care_location': services.location_service().get_location_by_id('8cb58fa5-1a6c-484b-ac9a-98cadb53064b'),
            'clinician': session['clinician'],
            'days_in_care': ''
        }

        metadata['templates']['appointments_container'] = render_template('appointments_container.html')
        metadata['templates']['appointments_item'] = render_template('patient/appointment_container_item.html')
        metadata['templates']['settings'] = render_template('patient/settings.html', context=metadata['settings'])

    except Exception as e:
        # Log error
        print("Some exception.. {}", e)
        raise

    appointments = {
        "text": "Appointments",
        "style": "active",
        "context": metadata['components'][0],
        "icon": "fas fa-calendar-alt"}

    return render_template('patient/index.html', title='Dashboard - Patient',
                           static_folder='patient.static',
                           style_paths=['css/appointment.css'],
                           script_paths=['js/appointment.js', 'js/main.js'],
                           nav_links=[appointments],
                           metadata=metadata)
