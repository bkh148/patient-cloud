import os
from flask import render_template, session, redirect, request, url_for, send_from_directory
from patient_portal.core.models import anonymous_required
app, socket_io = initialise_application("development")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


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


@app.route('/logout', methods=['POST'])
def logout():
    """Log the user out from the session, and clear session"""
    if 'user' in session:
        session.clear()
        return redirect(url_for('home_page'))


@app.errorhandler(404)
def not_found_error(error):
    """Handling 404 errors"""
    return render_template('404.html',
                           title="Page Not Found",
                           static_folder='static',
                           style_paths=
                           ['css/error_page.css']), 404

@app.errorhandler(500)
def internal_server_error(error):
    """Handling 500 errors"""
    return render_template('500.html', title="Internal Server Error", static_folder='static', style_paths=
                           ['css/error_page.css']), 500


