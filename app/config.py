import os
from dotenv import load_dotenv
load_dotenv()

# Use the process working directory as project root (Render sets cwd to repo src)
PROJECT_ROOT = os.getcwd()

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    DEBUG = False

    # Static folder under project_root/app/static
    STATIC_FOLDER = os.path.join(PROJECT_ROOT, 'app', 'static')
    # Uploads under static/uploads
    UPLOAD_FOLDER = os.path.join(STATIC_FOLDER, 'uploads')

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False