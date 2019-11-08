
__all__ = ['DevelopmentConfig', 'ProductionConfig']

class Config(object):
    API = ''

class DevelopmentConfig(Config):
    API = 'https://google.co.uk'
    MODE = 'Development Database'
    DATABASE_URI = 'patient_portal_development.db'

class ProductionConfig(Config):
    MODE = 'Production Database'
    DATABASE_URI = 'patient_portal_production.db'
