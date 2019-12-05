"""Module for managing any local admin sockets"""

from flask import session, request
from flask_socketio import disconnect
from .. import socket_io, services, online_local_admins
from ..core import authenticated_socket

@socket_io.on('connect', namespace='/local_admin')
def on_connect():
    user_id = session['user']['user_id']
    if user_id not in online_patients:
        online_local_admins[user_id] = request.sid

    
@socket_io.on('disconnect', namespace='/local_admin')
def on_disconnect():
    user_id = session['user']['user_id']
    if user_id in online_patients:
        online_local_admins.pop(user_id)

@socket_io.on('logout', namespace='/local_admin')
def logout(message):
    # To do: tidy up work to remove client from any necessary rooms
    print('Socket closed through logout')
    disconnect()
    