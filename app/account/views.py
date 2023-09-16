import hashlib
from flask_restful import Resource
from flask import request
from app.account.models import User
from app.account.forms import RegisterForm, LoginForm
from app.db import db
from app.config import Config


class Users(Resource):
    def get(self):
        users = User.query.all()
        return [
            {
                'id': row.id,
                'firstname': row.firstname,
                'lastname': row.lastname,
                'username': row.username,
                'email': row.email,
                'slug': row.slug,
            }
            for row in users
        ]

    def post(self):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            data = request.get_json()
            if data['type'] == 'register':
                del data['type']
                form = RegisterForm(data=data)
                if form.validate():
                    del data['confirm']
                    user = User(**data)
                    db.session.add(user)
                    db.session.commit()
                    return {
                        'message': 'ok'
                    }, 201
                else:
                    return {
                        "errors": form.errors
                    }, 400
            elif data['type'] == 'login':
                del data['type']
                form = LoginForm(data=data)
                if form.validate():
                    chaine_password = Config.SALT + data['password']
                    password = hashlib.md5(chaine_password.encode('utf8')).hexdigest()
                    row = db.session.query(User).filter_by(email=data['email'], password=password).first()
                    if row is None:
                        return {
                            "errors": {
                                "email": ["l'email ou le mot de passe ne correspondent pas"]
                            }
                        }
                    else:
                        return {
                            'message': 'ok',
                            'username': row.username,
                            'id': row.id,
                            'logged': True
                        }
                else:
                    return {
                        "errors": form.errors
                    }, 400
                return {
                    'message': 'login ok'
                }, 201
        return {
            'message': 'ko'
        }, 404
