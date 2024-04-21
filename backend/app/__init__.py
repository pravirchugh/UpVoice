import os
import pandas as pd
from flask import Flask
from flask_cors import CORS
from flask import current_app as app
from app.model import db

from app.api import api
from app.api.auth import auth
from app.api.stakeholder import stakeholder
from app.api.user import user
from app.api.voice import voice

from flask_jwt_extended import (
    create_access_token, JWTManager, jwt_required, 
    get_jwt_identity, create_refresh_token, 
    get_raw_jwt
)

from datetime import timedelta

def create_app(**config_overrides):
    app = Flask(__name__, instance_relative_config=True)

    cors = CORS(app)

    app.config.update(config_overrides)

    # Load config
    app.config.from_pyfile('settings.py')

    # Checking for email API key
    api_key = os.getenv('SENDGRID_API_KEY')
    if api_key is None:
        raise ValueError("SENDGRID_API_KEY is not set in the environment.")
    else:
        print("found the api key")

    # Initializing with JWT
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)  # define the life span of the token
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

    jwt = JWTManager(app) # initialize JWTManager

    blacklist = set()
    app.config['BLACKLIST'] = blacklist


    api.register_blueprint(stakeholder)
    api.register_blueprint(user)
    api.register_blueprint(voice)
    api.register_blueprint(auth)
    app.register_blueprint(api)

    return app