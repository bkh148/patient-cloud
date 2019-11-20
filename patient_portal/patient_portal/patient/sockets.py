"""Module for managing any patient sockets"""

from .. import socket_io
from flask_socketio import disconnect
from .. import services
from ..core import authenticated_socket

# Thoughts:
# The sockets shouldn't be responsible for the initial load of the dashboard.
# This should be up to the Jinja2 templates
#
# The Sockets should be responsible for adding the the users to the repective rooms
# in order to receive updates from any sup user, in the patient's case; the clinician
#

@socket_io.on('load_dashboard', namespace='/patient')
@authenticated_socket
def dashboard(message):
    print('Patient dashboard connection: {}'.format(message))

@socket_io.on('logout', namespace='/patient')
def logout(message):
    # To do: tidy up work to remove client from any necessary rooms
    print('Socket closed through logout')
    disconnect()
    
