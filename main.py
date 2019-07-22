import click
import os
from flask import Flask
from config import config

app = Flask(__name__)
app.config.from_object(config[os.getenv('FLASK_ENV')])

@app.route('/')
def home():
    return '<h1>Hello world</h1>'

from models import db, User
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User)

if __name__ == '__main__':
    app.run()