from flask_sqlalchemy import SQLAlchemy
from main import app

from datetime import datetime

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False, index=True)
    password = db.Column(db.String(256))
    posts = db.relationship('Post', backref='author')
    comments_made = db.relationship('Comment', backref='commentor')

    def __repr__(self):
        return f'<username: {self.username}>'

tags = db.Table(
    'posts_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512), nullable=False, index=True)
    content = db.Column(db.Text)
    published_date = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.relationship('Comment', backref='comments')
    tags = db.relationship(
        'Tag',
        secondary=tags,
        backref=db.backref('posts')
    )

    def __repr__(self):
        return f'<title: {self.title}>'

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False, unique=True, index=True)

    def __repr__(self):
        return f'<tag: {self.title}>'

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    commentor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.Column(db.Text, nullable=False)
    commented_date = db.Column(db.DateTime, default=datetime.now)
    commented_on_post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def __repr__(self):
        return f'<comment: {self.comment}>'

