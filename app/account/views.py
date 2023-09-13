from flask_restful import Resource
from flask import request
from app.account.models import User
from app.account.forms import RegisterForm
from app.db import db


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
        data = request.get_json()
        if data['type'] == 'register':
            form = RegisterForm(data=data)
            if form.validate():
                del data['type']
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
            return {
                'message': 'login ok'
            }, 201
        return {
            'message': 'ko'
        }, 404
