from datetime import datetime
from slugify import slugify
from app.db import db


class Post(db.Model):
    __tablename__ = 'blog_posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    slug = db.Column(db.String(128))
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.now)
    online = db.Column(db.Boolean)
    illustration = db.Column(db.String(255), default='https://placehold.it/850x350')

    categories = db.Column(db.Integer, db.ForeignKey('blog_categories.id'))
    authors = db.Column(db.Integer, db.ForeignKey('account_users.id'))
    comments = db.relationship('Comment', backref='blog_comments')

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def __str__(self):
        return '%s : %s' % (self.id, self.title)

    def __repr__(self):
        return '<%r %r %r>' % (__class__.__name__, self.id, self.title)

    def generate_slug(self):
        self.slug = ''
        if self.title:
            self.slug = slugify(self.title)
