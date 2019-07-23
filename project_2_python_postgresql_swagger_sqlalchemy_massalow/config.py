"""
	Config for all app
"""
import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the connexion application instance
connex_app = connexion.App(
    __name__, specification_dir=basedir + "/swagger-doc")

# Get the underlying Flask app instance
app = connex_app.app
