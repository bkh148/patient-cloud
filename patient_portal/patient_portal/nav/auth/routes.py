"""Module representing the authentication routes"""

from . import auth

# If authenticated, navigated to appropriate view (admin / norm)
#@auth.routes('/', methods=['GET', 'POST'])

# If user is already logged in, redirect to dashboard
@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Endpoint for handling user login."""
    return "Hello, login!"

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """Endpoint for handling user sign up."""
    return "Hello, sign up!"

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    """Endpoint for handling user logout."""
    return "Hello, logout!"
