from app.db import db


class Category(db.Model):
    __tablename__ = 'blog_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))
    posts = db.relationship('Post', backref='blog_categories')

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<{__class__.__name__} {self.name}>'
