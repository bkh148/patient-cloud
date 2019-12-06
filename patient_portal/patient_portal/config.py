
import os
from datetime import timedelta

__all__ = ['DevelopmentConfig', 'ProductionConfig']

class Config(object):
    MAIL_SERVER = os.environ['MAIL_SERVER'], #smtp.gmail.com
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = os.environ['MAIL_USERNAME'], #liamlambwebtech@gmail.com
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD'] #fglmcnthbmftkscd

class DevelopmentConfig(Config):
    MODE = 'Development'
    DEBUG = True
    HOST = '127.0.0.1'
    HOST_NAME = "127.0.0.1"
    PORT = 5000
    PERMANENT_SESSION_LIFETIME = timedelta(seconds=36000) # Session expire in 10 hours
    JWT_EXPIRATION_DELTA = timedelta(seconds=36000) # Token expire in 10 hours
    SECRET_KEY = 'MY_DEBUG_SECRETE_KEY'
    DATABASE_URI = 'patient_portal_development.db'

class ProductionConfig(Config):
    MODE = 'Production'
    DEBUG = False
    HOST = '0.0.0.0'
    HOST_NAME = "webtech-10.napier.ac.uk"
    PORT = 80
    PERMANENT_SESSION_LIFETIME = timedelta(seconds=3600) # Session expire in 1 hours
    JWT_EXPIRATION_DELTA = timedelta(seconds=3600) # Token expire in 1 hour
    SECRET_KEY = os.environ['SECRET_KEY']
    DATABASE_URI = 'patient_portal_production.db'
    
