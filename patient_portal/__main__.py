"""Module responsible for starting up the web application"""

from flask import render_template
from patient_portal import initialise_application

app = initialise_application("development")


@app.errorhandler(404)
def not_found_error(error):
    """Handling 404 errors"""
    return render_template('404.html', title="Page Not Found", style_paths=
            ['/static/css/error_page.css']), 404

@app.errorhandler(500)
def internal_server_error(error):
    """Handling 500 errors"""
    return render_template('500.html', title="Internal Server Error", style_paths=
            ['/static/css/error_page.css']), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
