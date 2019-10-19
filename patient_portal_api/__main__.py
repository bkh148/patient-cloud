"""Module responsible for starting up the patient portal REST API server"""""

from patient_portal_api import initialise_rest_server

rest_server = initialise_rest_server("configurations to come")

if __name__ == '__main__':
    rest_server.run(host='127.0.0.1', port='5001')
