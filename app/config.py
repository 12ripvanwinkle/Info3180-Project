import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    # Ensure DATABASE_URL is set in .env and use PostgreSQL URI format
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # To suppress the warning, and as it is deprecated
