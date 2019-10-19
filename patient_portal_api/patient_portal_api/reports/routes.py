"""Module for handling the reports RESTful routing"""

from . import reports

@reports.route('/v1', methods=['GET'])
def user_reports():
    """Handle some report request"""
    return "Hello, reports API!"
