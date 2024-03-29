"""Module for managing any clinician sockets"""

from flask import session, request, jsonify
from flask_socketio import disconnect
from .. import socket_io, services, online_clinicians, online_patients
from ..core import authenticated_socket


@socket_io.on('connect', namespace='/clinician')
def on_connect():
    user_id = session['user']['user_id']
    if user_id not in online_clinicians:
        online_clinicians[user_id] = request.sid


@socket_io.on('disconnect', namespace='/clinician')
def on_disconnect():
    user_id = session['user']['user_id']
    if user_id in online_clinicians:
        online_clinicians.pop(user_id)

    patients = services.user_service().get_all_users_patients(user_id)
    user_ids = [patient['user_id'] for patient in patients]
    patients_sid = {user_id: online_patients[user_id]
                    for user_id in user_ids if user_id in online_patients}

    # Notify all appropriate patients online that the clinician just went offline
    for patient_id, patient_sid in patients_sid.items():
        socket_io.emit('on_user_logout', {
                       'user_id': user_id, 'user_sid': request.sid}, namespace='/patient', room=patient_sid)


@socket_io.on('logout', namespace='/clinician')
def logout(message):
    disconnect()

@socket_io.on('notify_patient', namespace='/clinician')
def notify_patient(message):
    socket_io.emit(
        'on_send', message['data'], namespace='/patient', room=message['room_id'])
