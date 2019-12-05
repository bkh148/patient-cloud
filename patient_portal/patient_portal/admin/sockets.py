"""Module for managing any admin sockets"""

from flask import session, request
from flask_socketio import disconnect
from .. import socket_io, services, online_admins
from ..core import authenticated_socket

@socket_io.on('connect', namespace='/admin')
def on_connect():
    """On connect event with client's browser. This adds the the user's is and socket id to the in-memory cache."""
    user_id = session['user']['user_id']
    if user_id not in online_patients:
        online_admins[user_id] = request.sid

    
@socket_io.on('disconnect', namespace='/admin')
def on_disconnect():
    """On disconnect event with client's browser. This removes the the user's is and socket id from the in-memory cache."""
    user_id = session['user']['user_id']
    if user_id in online_patients:
        online_admins.pop(user_id)

@socket_io.on('logout', namespace='/admin')
def logout(message):
    disconnect()
    