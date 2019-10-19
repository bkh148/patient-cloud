"""Module for handling normal user routes"""

from . import nuser

@nuser.route('/', methods=['GET'])
@nuser.route('/dashboard', methods=['GET'])
def dashboard():
    """Handling the normal user dashboard"""
    return "Hello, nuser dashboard!"
