from pprint import pprint
from flask_restful import Resource
from flask import request
from app.db import db
from app.blog.models.comment import Comment


class Comments(Resource):
    def post(self):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            new_comment = Comment(**request.get_json())
            db.session.add(new_comment)
            db.session.commit()
            return {
                "message": "ok"
            }, 201
        return {
           "message": "ko"
        }, 400
