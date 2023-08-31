from flask import jsonify
from flask_restful import Resource, reqparse
from app.blog.models import Category
from slugify import slugify


class Categories(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id')
        super(Categories, self).__init__()

    def get(self):
        return jsonify({
            "categories": [{
                'name': row.name,
                'slug': slugify(row.name),
                'id': row.id
            } for row in Category.query.all()]
        })
