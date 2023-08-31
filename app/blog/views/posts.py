from flask_restful import Resource, reqparse
from app.blog.models import Post, Category
from app.account.models import User

class Posts(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id')
        super(Posts, self).__init__()

    def get(self):
        posts = Post.query.all()
        return {
            "posts": [{
                'id': row.id,
                'title': row.title,
                'slug': row.slug,
                'content': row.content,
                'author': User.query.get(row.authors).username,
                'categories': str(Category.query.get(row.categories)),
                'created': row.created.strftime("%d/%m/%Y")
            } for row in posts]
        } , 200
