# File: flask-backend/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from config import config_by_name
import routes
from dotenv import load_dotenv
import pymysql

# Install PyMySQL as MySQLdb
pymysql.install_as_MySQLdb()

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
config_name = os.getenv('FLASK_ENV') or 'development'
app.config.from_object(config_by_name[config_name])

# Configure MySQL connection via SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize MySQL for routes
routes.init_db(db)

# Enable CORS for all routes
CORS(app)

# Register Blueprints
app.register_blueprint(routes.todos_bp)

if __name__ == '__main__':
    app.run(debug=(config_name == 'development'))
