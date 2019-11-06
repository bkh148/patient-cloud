"""Module for managing any local admin sockets"""

from .. import socket_io


@socket_io.on('load_dashboard', namespace='/local_admin')
def dashboard(message):
    print('Local admin dashboard connection: {}'.format(message))
