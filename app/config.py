import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env if it exists.

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# Project root is one level up from app
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

class Config(object):
    """Base config for Flask application"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')

    # Static folder lives at project-root/static
    STATIC_FOLDER = os.path.join(PROJECT_ROOT, 'static')
    # Uploads go into static/uploads for simple static serving
    UPLOAD_FOLDER = os.path.join(STATIC_FOLDER, 'uploads')

    # Ensure DATABASE_URL is set in .env and use PostgreSQL URI format
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # To suppress the warning, and as it is deprecated

