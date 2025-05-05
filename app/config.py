import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env if it exists.

BASEDIR = os.path.abspath(os.path.dirname(__file__))
STATIC_FOLDER = os.path.join(BASEDIR, 'static')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    DEBUG = False

    # Point at app/static, not project-root/static
    UPLOAD_FOLDER = os.path.join(STATIC_FOLDER, 'uploads')

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
