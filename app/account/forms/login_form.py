import hashlib
import re
from flask_wtf import Form
from wtforms import StringField, PasswordField, validators
from app.config import Config
from app.db import db
from app.account.models import User


def is_email(form, field):
    pattern = re.compile(r'^([a-z0-9]+[-._]?[a-z0-9]+)+@([a-z0-9]+[-._]?[a-z0-9]+)+\.[a-z]{2,}$')
    if pattern.search(field.data) is None:
        raise validators.ValidationError("Cela ne correspond pas à un email valide")


class LoginForm(Form):
    email = StringField('Email', [
        validators.DataRequired(),
        validators.Length(min=3, max=64),
        is_email
    ])
    password = PasswordField('Mot de passe', [
        validators.DataRequired(),
    ])

