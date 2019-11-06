"""Module for managing any patient sockets"""

from .. import socket_io


@socket_io.on('load_dashboard', namespace='/patient')
def dashboard(message):
    print('Patient dashboard connection: {}'.format(message))
