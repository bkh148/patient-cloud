"""Module responsible for starting up the web application"""

from flask import render_template
from start_up import app, socket_io

if __name__ == '__main__':
    socket_io.run(app, host=app.config['HOST'],
                  port=app.config['PORT'], log_output=True)
