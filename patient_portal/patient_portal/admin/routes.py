"""Module for handling admin routes"""

from . import admin
from flask import render_template

# Route guarding requied
@admin.route('/', methods=['GET'])
@admin.route('/dashboard', methods=['GET'])
def dashboard():
    """Handle the admin dashboard"""
    return render_template('admin/index.html')

