"""[summary]
"""

import os
import urllib.parse

BASE_DIR = os.path.abspath(os.path.dirname(__file__))  


class Config:
    DEBUG = True


class ProductionConfig(Config):
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'TYHskdnwikdfndeifngeriwgnerog'
    DEBUG = False
  

class DevelopmentConfig(Config):
    SECRET_KEY = 'TYHskdnwikdfndeifngeriwgnerog'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    print(SQLALCHEMY_DATABASE_URI)



class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
