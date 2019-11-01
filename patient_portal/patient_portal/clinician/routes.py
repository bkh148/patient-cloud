"""Module for handling the clinician's content in the applciation"""

from . import clinician
from flask import render_template

@clinician.route('/', methods=['GET'])
@clinician.route('/dashboard', methods=['GET'])
def dashboard():
    """Handling the loading of the clinician's dashboard"""
    return render_template('clinician/index.html')
