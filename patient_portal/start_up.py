from flask import render_template
from patient_portal import initialise_application

app = initialise_application("development")

@app.route('/', methods=['GET'])
@app.route('/welcome', methods=['GET'])
def home_page():
    """First point of contact into the site.

    Todo:
        Route guarding is needed to redirect in case of authentication status (i.e. dashboard)
    """

    login = {
        'text': 'Login',
        'url': 'auth.login',
        'style': 'nav-link btn-success text-white text-center rounded m-2'}

    register = {
        'text': 'Register',
        'url': 'auth.register',
        'style': 'nav-link btn btn-danger text-white text-center rounded m-2'}

    return render_template('welcome.html', title='Welcome to Patient Portal', static_folder='static', style_paths=['css/auth.css'], nav_links=[login, register])

@app.errorhandler(404)
def not_found_error(error):
    """Handling 404 errors"""
    return render_template('404.html', title="Page Not Found", static_folder='static', style_paths=
                           ['css/auth.css', 'css/error_page.css']), 404

@app.errorhandler(500)
def internal_server_error(error):
    """Handling 500 errors"""
    return render_template('500.html', title="Internal Server Error", static_folder='static', style_paths=
                           ['css/auth.css', 'css/error_page.css']), 500

