"""File to intiate the create_app function that will define application that flask
will run on. Regiesters the blueprints here as well.
"""
import os
import urllib
from flask import Flask, Blueprint
from config import config
from .views.home.routes import main


def register_blueprints_on_app(app):
    app.register_blueprint(main)
 

def create_app(config_env='development', register_blueprints=True):

    app = Flask(__name__)

    app.config.from_object(config[config_env])

    if register_blueprints:
        register_blueprints_on_app(app)

    return app
