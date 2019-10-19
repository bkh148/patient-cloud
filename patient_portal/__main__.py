"""Module responsible for starting up the web application"""

from patient_portal import initialise_application

app = initialise_application("development")

if __name__ == '__main__':
    app.run()
