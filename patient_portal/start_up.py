import os
from flask import render_template, session, redirect, request, url_for, send_from_directory, abort
from patient_portal import initialise_application, services, jwt_manager
from pprint import pprint as pp
from patient_portal.core.models import anonymous_required
app, socket_io = initialise_application()

# Favicon Route
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Welcome Routes
@app.route('/', methods=['GET'])
@app.route('/welcome', methods=['GET'])
@anonymous_required
def home_page():
    """First point of contact into the site."""
    login = {
        'text': 'Login',
        'url': 'auth.login',
        'style': 'nav-link btn-success text-white text-center rounded m-2'}

    register = {
        'text': 'Register',
        'url': 'auth.register',
        'style': 'nav-link btn btn-danger text-white text-center rounded m-2'}

    return render_template('welcome.html',
                           title='Welcome to Patient Portal',
                           payload={
                               "welcome_message": "Wether you’re a local admin, clininian, or a patient - patient portal allows you to manage all of your medical data in one simple, intuitive and real-time application.",
                               "logo_doctor": "/static/images/doctor_lady_single.svg",
                               "version_number": "ver. 1.3.0"},
                           static_folder='static',
                           style_paths=['css/welcome.css'],
                           nav_links=[login, register])

# Catch all logout route
@app.route('/logout', methods=['POST'])
def logout():
    """Log the user out from the session, and clear session"""
    if 'user' in session:
        session.clear()
        return redirect(url_for('home_page'))


# Error route: 404
@app.errorhandler(404)
def not_found_error(error):
    """Handling 404 errors"""
    return render_template('404.html',
                           title="Page Not Found",
                           payload={
                               'message': 'Please follow the link below to bring you back to safety.',
                               'logo_doctor': '/static/images/doctor_sitting.svg'
                           },
                           static_folder='static',
                           style_paths=['css/error_page.css']), 404

# Error route 500
@app.errorhandler(500)
def internal_server_error(error):
    """Handling 500 errors"""
    return render_template('500.html',
                           title="Internal Server Error",
                           payload={
                               'message': 'Sorry about that, something went wrong on our end. Please follow the link to bring you back to safety.',
                               'logo_doctor': '/static/images/doctor_sitting.svg'
                           },
                           static_folder='static',
                           style_paths=['css/error_page.css']), 500


###################### Socket route handling ######################

@socket_io.on_error('/admin')
def admin_socket_error(error):
    print('SOCKET ADMIN ERROR: {}'.format(error))


@socket_io.on_error('/local_admin')
def local_admin_socket_error(error):
    print('SOCKET LOCAL ADMIN ERROR: {}'.format(error))


@socket_io.on_error('/clinician')
def clinician_socket_error(error):
    print('SOCKET CLINICIAN ERROR: {}'.format(error))


@socket_io.on_error('/patient')
def patient_socket_error(error):
    print('SOCKET PATIENT ERROR: {}'.format(error))
    
    
@jwt_manager.user_claims_loader
def add_claims_to_access_token(user):
    return {'role': user['role']}

@jwt_manager.user_identity_loader
def user_identity_lookup(user):
    return user['user_id']
