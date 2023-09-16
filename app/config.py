import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


class Config(object):
    ROOT = Path(__file__).resolve().parent.parent
    DEBUG = os.getenv('FLASK_DEBUG')
    SECRET_KEY = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SALT = '.7g^9Rh65vbfq/w)r]yn]eRgW;E/}-D6Y$%^vU3JyAW/473i4D27?dME4rk45r=e58=WZc6H)k_c~AMF-fhy~?8!T3D,:isnAj;JeLyz.Pn96Ntp6N$^762@i]_PH7Cbv7.Z*5Y}79(B4[+9:9t:d72~[e!6+8=9-N69w6Q,9B223U7,WTS_62fCFn@}S9k8ph3kGiP5Bwh6{FLA7i[Fw9j@?%ri2Nv67YJQRk%p{rR7Gyy87WQQ(9+EKQgY*!7{'

    @staticmethod
    def init_app(app):
        ...
