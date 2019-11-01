"""Module for handling admin routes"""

from . import admin
from flask import render_template

# Route guarding requied
@admin.route('/', methods=['GET'])
@admin.route('/dashboard', methods=['GET'])
def dashboard():
    """Handle the admin dashboard"""
    return render_template('admin/index.html', title='Dashboard - Admin', static_folder='admin.static', style_paths=
                           ['css/main.css'])

