"""Module for handling normal user routes"""

from . import patient
from flask import render_template

@patient.route('/', methods=['GET'])
@patient.route('/dashboard', methods=['GET'])
def dashboard():
    """Handling the normal patient dashboard"""
    return render_template('patient/index.html')
