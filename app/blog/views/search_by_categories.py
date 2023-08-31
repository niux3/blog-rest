from flask_restful import Resource
from app.blog.models import Post, Category
from app.account.models import User


class SearchByCategories(Resource):
    def get(self, id):
        posts = [
            {
                'id': row.id,
                'title': row.title,
                'slug': row.slug,
                'content': row.content,
                'author': User.query.get(row.authors).username,
                'categories': str(Category.query.get(row.categories)),
                'created': row.created.strftime("%d/%m/%Y")
            }
            for row in Post.query.filter(Post.categories==id)
        ]
        return {
            'posts': posts
        }, 200
