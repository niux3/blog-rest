from flask_restful import Resource
from app.blog.models import Post as PostModel, Category
from app.account.models import User
from markdown import markdown

class Post(Resource):
    def get(self, id):
        post = PostModel.query.get(id)
        user = User.query.get(post.authors)
        return {
            'id': post.id,
            'title': post.title,
            'content': markdown(post.content),
            'created': post.created.strftime("%d/%m/%Y"),
            'author': user.username,
            'categorie': str(Category.query.get(post.categories))
        }, 200
