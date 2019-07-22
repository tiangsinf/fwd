from flask_sqlalchemy import SQLAlchemy
from main import app

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, index=True)
    email = db.Column(db.String(128), nullable=False, index=True)
    password = db.Column(db.String(256))

    def __repr__(self):
        return f'id: {self.id}, email: {self.email}'