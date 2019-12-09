"""Module for managing any patient sockets"""

from flask import session, request
from flask_socketio import disconnect
from .. import socket_io, services, online_patients, online_clinicians
from ..core import authenticated_socket


@socket_io.on('connect', namespace='/patient')
def on_connect():
    user_id = session['user']['user_id']
    if user_id not in online_patients:
        online_patients[user_id] = request.sid

    clinician_user_id = session['clinician']['user_id']

    if clinician_user_id in online_clinicians:
        socket_io.emit('on_user_login', {'user_id': user_id, 'user_sid': request.sid},
                       namespace='/clinician', room=online_clinicians[clinician_user_id])


@socket_io.on('disconnect', namespace='/patient')
def on_disconnect():
    user_id = session['user']['user_id']
    if user_id in online_patients:
        online_patients.pop(user_id)

    clinician_user_id = session['clinician']['user_id']

    if clinician_user_id in online_clinicians:
        socket_io.emit('on_user_logout', {
                       'user_id': user_id}, namespace='/clinician', room=online_clinicians[clinician_user_id])


@socket_io.on('logout', namespace='/patient')
def logout(message):
    disconnect()
