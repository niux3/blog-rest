from flask_restful import Resource
from app.account.models import User


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
