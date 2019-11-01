"""Module for handling normal user routes"""

from . import patient
from flask import render_template

@patient.route('/', methods=['GET'])
@patient.route('/dashboard', methods=['GET'])
def dashboard():
    """Handle the patient dashboard"""
    return render_template('patient/index.html', title='Dashboard - Patient', static_folder='patient.static', style_paths=
                           ['css/main.css'])
