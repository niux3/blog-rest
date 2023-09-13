import re
from flask_wtf import Form
from wtforms import StringField, EmailField, PasswordField, validators
from app.db import db
from app.account.models import User

def is_username_unique(form, field):
    data = db.session.query(User).filter(User.username==field.data).first()
    if data is not None:
        raise validators.ValidationError("Ce pseudonyme existe déjà")


def is_email_unique(form, field):
    data = db.session.query(User).filter(User.email==field.data).first()
    if data is not None:
        raise validators.ValidationError("Cet email existe déjà")


def is_email(form, field):
    pattern = re.compile(r'^([a-z0-9]+[-._]?[a-z0-9]+)+@([a-z0-9]+[-._]?[a-z0-9]+)+\.[a-z]{2,}$')
    if pattern.search(field.data) is None:
        raise validators.ValidationError("Cela ne correspond pas à un email valide")


class RegisterForm(Form):
    firstname = StringField('Prénom')
    lastname = StringField('Nom', [
        validators.DataRequired(),
        validators.Length(min=3, max=64)
    ])
    username = StringField('Psuedo', [
        validators.DataRequired(),
        validators.Length(min=3, max=64),
        is_username_unique
    ])
    email = StringField('Email', [
        validators.DataRequired(),
        validators.Length(min=3, max=64),
        is_email_unique,
        is_email
    ])
    password = PasswordField('Mot de passe', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message="Ce champ doit être identique à la confirmation"),
    ])
    confirm = PasswordField('confirmation mot de passe', [
        validators.DataRequired(),
        validators.EqualTo('password', message="Ce champ doit être identique au mot de passe"),
    ])
