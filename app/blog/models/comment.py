from datetime import datetime
from app.db import db


class Comment(db.Model):
    __tablename__ = 'blog_comments'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    online = db.Column(db.Boolean, default=True)

    posts = db.Column(db.Integer, db.ForeignKey('blog_posts.id'))
    authors = db.Column(db.Integer, db.ForeignKey('account_users.id'))

    def __str__(self):
        return '%s : %s - %s' % (self.id, self.authors, self.posts)

    def __repr__(self):
        return '<%r %r %r %r>' % (__class__.__name__, self.id, self.authors, self.posts)
