from flask import Blueprint
from flask_restplus import Api
from .api import *


api_v1 = Blueprint('api', __name__, url_prefix='/api/v1.0')
api = Api(api_v1, 
    title='Patient Portal Api',
    version='1.0',
    description="Some Patient Portal description",
)


api.add_namespace(authentication_nsp)
api.add_namespace(appointment_nsp)
api.add_namespace(location_nsp)
api.add_namespace(invitation_nsp)
api.add_namespace(log_nsp)
