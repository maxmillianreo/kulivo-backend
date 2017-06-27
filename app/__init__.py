# app/__init__.py

# third-party imports
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# local imports
from config import app_config

flaskapp = Flask(__name__)
flaskapp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://superadmin:admin111@35.185.177.69/db_kulivo'
# db variable initialization
db = SQLAlchemy(flaskapp)
login_manager = LoginManager()

#import route
import app.views
