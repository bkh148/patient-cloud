"""Module for managing any clinician sockets"""

from .. import socket_io


@socket_io.on('load_dashboard', namespace='/clinician')
def dashboard(message):
    print('Clinician dashboard connection: {}'.format(message))
