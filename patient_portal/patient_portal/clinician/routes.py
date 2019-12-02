"""Module for handling the clinician's content in the applciation"""

from . import clinician
from flask import render_template, session
from .. import services
from ..core import login_required, UserRole

@clinician.route('/', methods=['GET'])
@clinician.route('/dashboard', methods=['GET'])
@login_required('CLINICIAN')
def dashboard():
    """Handle the clincian dashboard"""

    metadata = {
        'appointments': {},
        'patients': '',
        'configurations': {},
        'templates': {},
        'components': ['patients', 'appointments', 'settings'],
        'settings': {},
        'online_users': {},
        'user_roles': {}
    }

    try:
        metadata['appointments'] = services.appointment_service().get_appointments_created_by(session['user']['user_id'])
        metadata['patients'] = services.user_service().get_all_users_patients(session['user']['user_id'])
        metadata['user_roles'] = services.user_service().get_user_role_ids([UserRole.PATIENT.value])
        metadata['settings'] = {
            'user': session['user'],
            "care_location": services.location_service().get_location_by_id('8cb58fa5-1a6c-484b-ac9a-98cadb53064b'),
            "active_account": 1,
            "stay_logged_in": 1}

        metadata['configurations'] = {
            "host": "127.0.0.1",
            "port": "5000",
            "namespace": "clinician",
            "session_id": session['session_id']}

        # Todo: Create a clinician's patient view
        metadata['templates']['users_container'] = render_template('clinician/users_container_override.html', 
                                                                   title='Your Patients', 
                                                                   subtitle_one='Currently in your care', 
                                                                   subtitle_two='Previously in your care',
                                                                   modal_title='Invite a Patient')
        metadata['templates']['patient_item'] = 'Patient'
        metadata['templates']['appointments_container'] = render_template('appointments_container.html')
        metadata['templates']['appointments_item'] = render_template('clinician/appointment_container_item.html')
        metadata['templates']['settings'] = render_template(
            'clinician/settings.html', context=metadata['settings'])

    except Exception as e:
        # Log this through the log service..
        print('Some exception: {}'.format(e))

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
                           script_paths=['js/appointment.js', 'js/invite.js', 'js/patients.js', 'js/main.js'],
                           nav_links=[patients, appointments],
                           metadata=metadata)
