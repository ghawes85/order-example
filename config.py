"""[summary]
"""

import os
import urllib.parse



class Config:
    DEBUG = True


class ProductionConfig(Config):
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'TYHskdnwikdfndeifngeriwgnerog'
    DEBUG = False
  

class DevelopmentConfig(Config):
    SECRET_KEY = 'TYHskdnwikdfndeifngeriwgnerog'
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
