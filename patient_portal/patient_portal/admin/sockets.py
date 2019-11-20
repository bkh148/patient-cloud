"""Module for managing any admin sockets"""

from .. import socket_io
from flask_socketio import disconnect
from .. import services
from ..core import authenticated_socket


@socket_io.on('load_dashboard', namespace='/admin')
@authenticated_socket
def dashboard(message):
    print('Admin dashboard connection: {}'.format(message))


@socket_io.on('logout', namespace='/admin')
def logout(message):
    # To do: tidy up work to remove client from any necessary rooms
    print('Socket closed through logout')
    disconnect()
    