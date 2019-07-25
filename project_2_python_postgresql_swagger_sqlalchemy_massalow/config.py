"""
	Config for all app
"""
import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# Get current directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Create the connexion application instance
connex_app = connexion.App(
    __name__, specification_dir=basedir + "/swagger-doc")

# Get the underlying Flask app instance
app = connex_app.app

# Base connection URL
sqlite_url = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}:{PORT}/{DB_NAME}".format(
    DB_USER="postgres", DB_PASS="112297607", DB_ADDR="127.0.0.1", PORT="5432", DB_NAME="vnas")

# Config connect to Database
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SqlAlchemy db instance
db = SQLAlchemy(app)
CORS(app)

# Initialize Marshmallow
ma = Marshmallow(app)
