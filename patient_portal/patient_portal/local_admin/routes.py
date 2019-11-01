"""Module for handling the local admin requests"""

from . import local_admin
from flask import render_template

@local_admin.route('/', methods=['GET'])
@local_admin.route('/dashboard', methods=['GET'])
def dashboard():
    """Handling the local admin's dashboard"""
    return render_template('local_admin/index.html')
