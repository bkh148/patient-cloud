"""Module for handling admin routes"""

from . import admin
from flask import render_template

# Route guarding requied
@admin.route('/', methods=['GET'])
@admin.route('/dashboard', methods=['GET'])
def dashboard():
    """Handle the admin dashboard"""

    dashboard = {
        "text": "Dashboard",
        "style": "active",
        "url": "",
        "icon": "fas fa-home"}

    care_locations = {
        "text": "Care Locations",
        "style": "",
        "url": "",
        "icon": "fas fa-hospital-alt"}

    data_analytics = {
        "text": "Analytics",
        "style": "",
        "url": "",
        "icon": "fas fa-chart-line"}

    return render_template('admin/index.html', title='Dashboard - Admin', static_folder='admin.static', style_paths=
                           ['css/main.css'], nav_links=[dashboard, care_locations, data_analytics])

