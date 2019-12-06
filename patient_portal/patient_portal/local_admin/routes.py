"""Module for handling the local admin requests"""

from . import local_admin
from flask import render_template, session
from .. import services, app
from ..core import login_required


@local_admin.route('/', methods=['GET'])
@local_admin.route('/dashboard', methods=['GET'])
@login_required('LOCAL_ADMIN')
def dashboard():
    """Handle the local admin dashboard"""

    metadata = {
        'clinicians': [],
        'configurations': {},
        'templates': {},
        'components': ['clinicians', 'settings'],
        'settings': {},
        'online_users': {}
    }

    try:

        # Pull from session object
        metadata['clinicians'] = []
        metadata['components'] = ['clinicians', 'settings']
        metadata['settings'] = {
            'user': session['user'],
            "active_account": 1,
            "stay_logged_in": 1}

        metadata['configurations'] = {
            "host": app.config['HOST'],
            "port": app.config['PORT'],
            "namespace": "local_admin",
            "session_id": session['session_id']}

    except Exception as e:
        # Log error
        print('Some exception {}'.format(e))

    clinicians = {
        "text": "Clinicians",
        "style": "active",
        "context": metadata['components'][0],
        "icon": "fas fa-user-md"}

    metadata['templates']['clinicians'] = render_template('local_admin/users_container_override.html',
                                                          title='Your Clinicians',
                                                          invite_icon='fas fa-user-md',
                                                          subtitle_one='Currently in this care location',
                                                          subtitle_two='Previously in this care location',
                                                          modal_title='Invite a Clinician')
    metadata['templates']['settings'] = render_template(
        'local_admin/settings.html', context=metadata['settings'])
    metadata['templates']['notification'] = render_template(
        'notification.html')

    return render_template('local_admin/index.html', title='Dashboard - Local Admin',
                           static_folder='local_admin.static',
                           style_paths=['css/main.css'],
                           script_paths=['js/invite.js', 'main.js'],
                           nav_links=[clinicians],
                           metadata=metadata)
