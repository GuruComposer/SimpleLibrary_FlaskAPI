from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# Config
app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)