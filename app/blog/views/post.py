from flask_restful import Resource
from app.blog.models import Post as PostModel, Category, Comment
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
            'comments': [
               {
                   'title': row_c.title,
                   'content': markdown(row_c.content),
                   'created': row_c.created.strftime('%d/%m/%Y'),
                   'author': str(User.query.get(row_c.authors).username)
               }
               for row_c in Comment.query.filter(Comment.online == True, Comment.posts == post.id)
            ],
            'illustration': post.illustration,
            'categorie': str(Category.query.get(post.categories))
        }, 200
