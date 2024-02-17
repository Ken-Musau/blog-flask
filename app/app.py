from flask import Flask, jsonify, make_response
from flask_migrate import Migrate

from models import db, Post, Author, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route("/")
def welcome():
    return "<h1>Welcome to my blog </h2>"


@app.route("/posts")
def posts():
    posts = [post.to_dict() for post in Post.query.all()]
    return make_response(jsonify(posts), 200)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
