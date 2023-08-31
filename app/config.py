import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


class Config(object):
    ROOT = Path(__file__).resolve().parent.parent
    DEBUG = os.getenv('FLASK_DEBUG')
    SECRET_KEY = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    @staticmethod
    def init_app(app):
        ...
