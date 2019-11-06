"""Module for managing any admin sockets"""

from .. import socket_io


@socket_io.on('load_dashboard', namespace='/admin')
def dashboard(message):
    print('Admin dashboard connection: {}'.format(message))
