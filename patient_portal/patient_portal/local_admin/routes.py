"""Module for handling the local admin requests"""

from . import local_admin

@local_admin.route('/', methods=['GET'])
@local_admin.route('/dashboard', methods=['GET'])
def dashboard():
    """Handling the local admin's dashboard"""
    return "Local admin dashboard"
