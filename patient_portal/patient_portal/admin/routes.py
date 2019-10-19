"""Module for handling admin routes"""

from . import admin

# Route guarding requied
@admin.route('/', methods=['GET'])
@admin.route('/dashboard', methods=['GET'])
def dashboard():
    """Handle the admin dashboard"""
    return "Hello, admin dashboard!"

