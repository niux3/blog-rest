from flask_restful import Resource, reqparse
from app.blog.models import Post, Category, Comment
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
                'illustration': row.illustration,
                'comments': [
                    {
                        'title': row_c.title,
                        'content': row_c.content,
                        'created': row_c.created.strftime('%d/%m/%Y'),
                        'author': str(User.query.get(row_c.authors).username)
                    }
                    for row_c in Comment.query.filter(Comment.online==True, Comment.posts==row.id)
                ],
                'created': row.created.strftime("%d/%m/%Y")
            } for row in posts]
        } , 200
