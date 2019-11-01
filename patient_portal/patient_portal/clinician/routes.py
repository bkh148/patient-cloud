"""Module for handling the clinician's content in the applciation"""

from . import clinician

@clinician.route('/', methods=['GET'])
@clinician.route('/dashboard', methods=['GET'])
def dashboard():
    """Handling the loading of the clinician's dashboard"""
    return "Clinician Dashboard"
