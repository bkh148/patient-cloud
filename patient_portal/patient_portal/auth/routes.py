"""Module representing the authentication routes"""

from flask import render_template, flash, session, request, redirect, url_for, json, make_response, abort
from . import auth
import uuid
from .. import services
from datetime import datetime
from ..core.models import UserRole, anonymous_required
from werkzeug.security import generate_password_hash

# If user is already logged in, redirect to dashboard
@auth.route('/login', methods=['GET', 'POST'])
@anonymous_required
def login():
    """Endpoint for handling user login."""

    validation_error = {}

    if request.method == "POST":

        user_mail = request.form.get('email', None)
        user_pwd = request.form.get('password', None)
        user = services.user_service().validate_user(user_mail, user_pwd)

        if user:
            session['user'] = user
            for role in UserRole:
                if user['role'] == role.value:
                    session['session_id'] = str(uuid.uuid4())
                    return redirect(url_for('{}.dashboard'.format(role.value.lower())))
                else:
                    validation_error['authentication_error'] = 'An error has occurred logging you in.'
        else:
            validation_error['authentication_error'] = 'Unrecognized e-mail & password combination.'

    return render_template('auth/login.html',
                           title='Login',
                           static_folder='auth.static',
                           script_paths=['js/auth.js'],
                           style_paths=['css/auth.css'],
                           error=validation_error)


@auth.route('/invite/<string:invite_id>', methods=['GET', 'POST'])
@anonymous_required
def register(invite_id):

    invite = services.invite_service().get_invite_by_id(invite_id)

    if invite:
        # If the invite hasn't expired, process it, and update it, then redirect user
        # DANGER: This is a temporary date parsing solution due to the python version I need to use.. Python 3.7 handles ISO parsing properly
        expire_date = datetime.strptime(
            invite['expiration_date_utc'], "%Y-%m-%dT%H:%M:%SZ")

        if datetime.utcnow() < expire_date and not bool(int(invite['is_consumed'])):
            messages = {}
            if request.method == "POST":
                try:

                    # Create a new user role map entry
                    user_role_map = {
                        'user_role_map_id': str(uuid.uuid4()),
                        'user_role_id': invite['user_role_id'],
                        'location_id': invite['assign_to_location']
                    }

                    # Create a new user from the form
                    user = {
                        'user_id': str(uuid.uuid4()),
                        'user_role_map_id': user_role_map['user_role_map_id'],
                        'user_email': invite['invited_email'],
                        'user_forename': request.form.get('forename', invite['invited_forename']),
                        'user_surname': request.form.get('surname', invite['invited_surname']),
                        'user_dob': request.form.get('dob')
                    }

                    services.user_service().upsert_user_role_map(user_role_map)
                    services.user_service().upsert_user(user)
                    services.password_service().upsert_password(
                        user['user_id'], generate_password_hash(request.form.get('password')))
                    user_role = services.user_service().get_user_role(
                        invite['user_role_id'])

                    # If this is a patient, we need to create a mapping with their clinician:
                    if user_role['user_role'] == UserRole.PATIENT.value:
                        services.user_service().upsert_patient_clinician_map(
                            invite['invited_by'], user['user_id'])

                    invite['is_consumed'] = '1'
                    services.invite_service().upsert_invite(invite)

                    messages['authentication_success'] = "You have successfully created your account."

                    return render_template('auth/invite_credentials.html',
                                           title='Create Login',
                                           invite=invite,
                                           messages=messages,
                                           static_folder='auth.static',
                                           style_paths=['css/auth.css'],
                                           script_paths=['js/auth.js']), 200

                except Exception as e:
                    services.log_service().log_exception(e)
                    messages['authentication_error'] = "An error has occurred whilst creating your credentials."

                    return render_template('auth/invite_credentials.html',
                                           title='Create Login',
                                           invite=invite,
                                           messages=messages,
                                           static_folder='auth.static',
                                           style_paths=['css/auth.css'],
                                           script_paths=['js/auth.js']), 500

            else:
                return render_template('auth/invite_credentials.html',
                                       title='Create Login',
                                       invite=invite,
                                       messages=messages,
                                       static_folder='auth.static',
                                       style_paths=['css/auth.css'],
                                       script_paths=['js/auth.js']), 200

        else:
            abort(404)
    else:
        abort(404)

    """Register user's invitation from the e-mail redirect"""
    return render_template('welcome.html',
                           title='Welcome to Patient Portal',
                           payload={
                               "welcome_message": "Wether you’re a local admin, clininian, or a patient - patient portal allows you to manage all of your medical data in one simple, intuitive and real-time application.",
                               "logo_doctor": "/static/images/doctor_lady_single.svg",
                               "version_number": "ver. 1.3.0"},
                           static_folder='static',
                           style_paths=['css/welcome.css'],
                           nav_links=[login, register])
