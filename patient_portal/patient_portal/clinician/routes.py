"""Module for handling the clinician's content in the applciation"""

from . import clinician
from flask import render_template
from .. import services

@clinician.route('/', methods=['GET'])
@clinician.route('/dashboard', methods=['GET'])
def dashboard():
    """Handle the clincian dashboard"""

    metadata = {}
    metadata['appointments'] = {}

    # Get the following from the session when authentication is setup
    metadata['settings'] = {}
    metadata['configurations'] = {}
    metadata['components'] = []
    metadata['patients'] = []

    try:
        appointments = []
        metadata['appointments']['upcoming'] = appointments
        metadata['patients'] = services.user_service().get_all_users_patients('b587e97b-5ccc-4f4d-ae65-c507a268e1bb')
        metadata['components'] = ['patients', 'appointments', 'settings']
        metadata['settings'] = {
            "forename": "Clinician",
            "surname": "A",
            "email": "clinician@hospital.co.uk",
            "care_location": "Chalmers Hospital",
            "care_location_id": "some_id",
            "active_account": 1,
            "stay_logged_in": 1}
        
        metadata['configurations'] = {
        "host": "127.0.0.1",
        "port": "5000",
        "namespace": "clinician"}
        
    except Exception as e:
        # Log this through the log service..
        print('Some exception')

    patients = {
        "text": "Patients",
        "style": "active",
        "context": metadata['components'][0],
        "icon": "fas fa-procedures"}

    appointments = {
        "text": "Appointments",
        "style": "",
        "context": metadata['components'][1],
        "icon": "fas fa-calendar-check"}

    return render_template('clinician/index.html', title='Dashboard - Clinician',
                           static_folder='clinician.static',
                           style_paths=['css/main.css'],
                           nav_links=[patients, appointments],
                           metadata=metadata)
