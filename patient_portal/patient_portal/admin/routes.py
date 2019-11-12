"""Module for handling admin routes"""

from . import admin
from flask import render_template
from .. import services

# Route guarding requied
@admin.route('/', methods=['GET'])
@admin.route('/dashboard', methods=['GET'])
def dashboard():
    """Handle the admin dashboard"""

    metadata = {}
    metadata['care_locations'] = []
    metadata['data_analytics'] = {}
    metadata['components'] = []
    metadata['settings'] = {}

    try:
        data_analysis = []
        metadata['care_locations'] = services.location_service().get_all_locations()
        metadata['data_analytics'] = data_analysis
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
        "namespace": "admin"}

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

    return render_template('admin/index.html', title='Dashboard - Admin', static_folder='admin.static',
                           style_paths=['css/main.css'],
                           nav_links=[care_locations, data_analytics],
                           metadata=metadata)

