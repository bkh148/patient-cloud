"""Module for handling normal user routes"""

from . import patient

@patient.route('/', methods=['GET'])
@patient.route('/dashboard', methods=['GET'])
def dashboard():
    """Handling the normal patient dashboard"""
    return "Hello, nuser dashboard!"
