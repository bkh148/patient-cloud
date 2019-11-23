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
        'settings': {}
    }

    try:
        metadata['appointments']['upcoming'] = services.appointment_service().get_appointments_for(session['user']['user_id'])
        
        # Get from session
        metadata['configurations'] = {
        "host": "127.0.0.1",
        "port": "5000",
        "namespace": "patient",
        "session_id": session['session_id']}
        
        # Get the following from the session when authentication is setup
        metadata['settings'] = {
            'user_email': 'liam.j.lamb@gmail.com',
            'user_forname': 'Liam',
            'user_surname': 'Lamb',
            'remember_me': 0,
            'care_location': services.location_service().get_location_by_id('8cb58fa5-1a6c-484b-ac9a-98cadb53064b'),
            'clinician': services.user_service().get_patient_clinician('c5739269-355b-497e-8249-ce4ffce8b020'),
            'days_in_care': ''
        }

        metadata['templates']['appointments_container'] = render_template('appointments_container.html')
        metadata['templates']['appointments_item'] = render_template('appointment_container_item.html')
        metadata['templates']['settings'] = render_template('patient/settings.html', context=metadata['settings'])

    except Exception as e:
        # Log error
        print("Some exception.. {}", e)
        raise

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
