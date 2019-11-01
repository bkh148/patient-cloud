"""Module for handling the clinician's content in the applciation"""

from . import clinician
from flask import render_template

@clinician.route('/', methods=['GET'])
@clinician.route('/dashboard', methods=['GET'])
def dashboard():
    """Handle the clincian dashboard"""
    return render_template('clinician/index.html', title='Dashboard - Clinician', static_folder='clinician.static', style_paths=
                           ['css/main.css'])
