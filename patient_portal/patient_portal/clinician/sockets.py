"""Module for managing any clinician sockets"""

from .. import socket_io
from flask_socketio import disconnect
from .. import services
from ..core import authenticated_socket

@socket_io.on('load_dashboard', namespace='/clinician')
@authenticated_socket
def dashboard(message):
    print('Clinician dashboard connection: {}'.format(message))

@socket_io.on('logout', namespace='/clinician')
def logout(message):
    # To do: tidy up work to remove client from any necessary rooms
    print('Socket closed through logout')
    disconnect()
    