"""Module for handling admin routes"""

from . import admin
from flask import render_template, session, request
from .. import services
from ..core import login_required
from flask_jwt_extended import create_access_token, create_refresh_token

# Route guarding requied
@admin.route('/', methods=['GET'])
@admin.route('/dashboard', methods=['GET'])
@login_required('ADMIN')
def dashboard():
    """Handle the admin dashboard"""

    metadata = {
        'data_analytics': {},
        'care_locations': [],
        'configurations': {},
        'templates': {},
        'components': ['care_locations', 'data_analytics', 'settings'],
        'settings': {},
        'online_users': {}
    }

    try:
        metadata['care_locations'] = services.location_service().get_all_locations()
        metadata['data_analytics'] = []
        metadata['components'] = ['care_locations', 'data_analytics', 'settings']

        metadata['settings'] = {
            "forename": "Admin",
            "surname": "AdminSur",
            "email": "admin@royal.nhs.co.uk",
            "active_account": 1,
            "stay_logged_in": 0
        }

        metadata['configurations'] = {
        "host": "127.0.0.1",
        "port": "5000",
        "namespace": "admin",
        "session_id": session['session_id'],
        "access_token": create_access_token(identity=session['user']),
        "refresh_token": create_refresh_token(session['user'])}

    except Exception as e:
        # Log error
        print('Some exception {}'.format(e))

    care_locations = {
    "text": "Care Locations",
    "style": "active",
    "context": metadata['components'][0],
    "icon": "fas fa-hospital-alt"}

    data_analytics = {
    "text": "Analytics",
    "style": "",
    "context": metadata['components'][1],
        "icon": "fas fa-chart-line"}


    metadata['templates']['care_locations'] = 'Hello, care locations'
    metadata['templates']['data_analytics'] = 'Hello, data analytics'
    metadata['templates']['settings'] = render_template('admin/settings.html', context=metadata['settings'])


    return render_template('admin/index.html', title='Dashboard - Admin', static_folder='admin.static',
                           style_paths=['css/main.css'],
                           script_paths=['js/invite.js'],
                           nav_links=[care_locations, data_analytics],
                           metadata=metadata)

