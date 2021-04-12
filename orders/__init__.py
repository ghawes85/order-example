"""File to intiate the create_app function that will define application that flask
will run on. Regiesters the blueprints here as well.
"""
import os
import urllib
from flask import Flask, Blueprint
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

sqlalchemy = SQLAlchemy()
migrate = Migrate()


def register_blueprints_on_app(app):
    # import blueprints here to avoid circular import issues
    from .views.home import main
    
    app.register_blueprint(main)


def create_app(config_env="development", register_blueprints=True):

    app = Flask(__name__)

    app.config.from_object(config[config_env])
    sqlalchemy.init_app(app)
    migrate.init_app(app, sqlalchemy)

    if register_blueprints:
        register_blueprints_on_app(app)

    return app
