"""Module for handling the local admin requests"""

from . import local_admin
from flask import render_template

@local_admin.route('/', methods=['GET'])
@local_admin.route('/dashboard', methods=['GET'])
def dashboard():
    """Handle the local admin dashboard"""

    dashboard = {
        "text": "Dashboard",
        "style": "active",
        "url": "",
        "icon": "fas fa-home"}

    clinicians = {
        "text": "Clinicians",
        "url": "",
        "style": "",
        "icon": "fas fa-user-md"}

    appointments = {
        "text": "Appointments",
        "url": "",
        "style": "",
        "icon": "fas fa-calendar-check"}

    return render_template('local_admin/index.html', title='Dashboard - Local Admin', static_folder='local_admin.static', style_paths=
                           ['css/main.css'], nav_links=[dashboard, clinicians, appointments])
