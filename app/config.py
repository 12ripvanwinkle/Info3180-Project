import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env if it exists.



class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    STATIC_FOLDER = os.path.join(BASE_DIR, 'static')
    UPLOAD_FOLDER = os.path.join(STATIC_FOLDER, os.getenv('UPLOAD_FOLDER'))

    # Ensure DATABASE_URL is set in .env and use PostgreSQL URI format
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # To suppress the warning, and as it is deprecated

