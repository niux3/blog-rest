import hashlib
from datetime import datetime
from slugify import slugify
from app.db import db


class User(db.Model):
    __tablename__ = 'account_users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), nullable=True)
    lastname = db.Column(db.String(64))
    username = db.Column(db.String(16), unique=True)
    slug = db.Column(db.String(128))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(32))
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.now)

    posts = db.relationship('Post', backref='account_users')
    comments = db.relationship('Comment', backref='account_users')

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()
        self.generate_password()

    def __str__(self):
        return '%s : %s' % (self.id, self.email)

    def __repr__(self):
        return '<%r %r %r>' % (__class__.__name__, self.id, self.email)

    def generate_slug(self):
        self.slug = ''
        if self.lastname:
            self.slug = slugify(f'{self.id}-{self.lastname}')

    def generate_password(self):
        self.password = hashlib.md5(self.password.encode('utf-8')).hexdigest()

