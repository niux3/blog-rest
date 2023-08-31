from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from app.config import Config
from app.db import db
from app.account.views import Users
from app.blog.views import (
    Posts,
    Categories,
    Post as PostShow,
    SearchByCategories,
    Comments
)


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    Config.init_app(app)

    db.init_app(app)
    migrate = Migrate()

    from app.blog.models import Post, Category, Comment
    from app.account.models import User
    migrate.init_app(app, db, directory=Config.ROOT /'app'/'migrations')

    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    api = Api(app)

    api.add_resource(Posts, '/posts', endpoint='posts')
    api.add_resource(PostShow, '/post/<int:id>', endpoint='post')
    api.add_resource(Categories, '/categories', endpoint='categories')
    api.add_resource(SearchByCategories, '/search-categories/<int:id>', endpoint='search_categories')
    api.add_resource(Users, '/users', endpoint='users')
    api.add_resource(Comments, '/comments', endpoint='comments')

    return app

