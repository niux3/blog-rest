from flask_restful import Resource
from app.blog.models import Post, Comment, Category
from app.account.models import User


class SearchByAuthors(Resource):
    def get(self, id):
        posts = [
            {
                'id': row.id,
                'title': row.title,
                'slug': row.slug,
                'content': row.content,
                'illustration': row.illustration,
                'author': User.query.get(row.authors).username,
                'categories': str(Category.query.get(row.categories)),
                'comments': [
                    {
                        'title': row_c.title,
                        'content': row_c.content,
                        'created': row_c.created.strftime('%d/%m/%Y'),
                        'author': str(User.query.get(row_c.authors).username)
                    }
                    for row_c in Comment.query.filter(Comment.online == True, Comment.posts == row.id)
                ],
                'created': row.created.strftime("%d/%m/%Y")
            }
            for row in Post.query.filter(Post.authors == id)
        ]
        return {
            'posts': posts
        }, 200
