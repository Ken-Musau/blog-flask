from flask import Flask, jsonify, make_response, request
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


@app.route("/posts", methods=["GET", "POST"])
def posts():
    if request.method == "GET":
        posts = [post.to_dict() for post in Post.query.all()]
        return make_response(jsonify(posts), 200)

    elif request.method == "POST":
        new_post = Post(
            title=request.form.get("title"),
            content=request.form.get("content")
        )

        db.session.add(new_post)
        db.session.commit()

        post_dict = new_post.to_dict()

        return make_response(jsonify(post_dict), 200)


@app.route("/posts/<int:id>", methods=["GET", "PATCH", "DELETE"])
def post_by_id(id):

    post = Post.query.filter_by(id=id).first()

    if request.method == "GET":
        post_dict = post.to_dict()

        return make_response(jsonify(post_dict), 200)

    elif request.method == "PATCH":
        for attr in request.form:
            setattr(post, attr, request.form.get(attr))

            db.session.add(post)
            db.session.commit()

            post_dict = post.to_dict()

            return make_response(jsonify(post_dict), 200)

    elif request.method == "DELETE":
        db.session.delete(post)
        db.session.commit()

        return make_response([
            "Post has been deleted"
        ])


@app.route("/comments", methods=["GET", "POST"])
def comments():
    if request.method == "GET":
        comments = [comment.to_dict() for comment in Comment.query.all()]
        return make_response(jsonify(comments), 200)

    elif request.method == "POST":
        new_comment = Comment(
            content=request.form.get("content"),
            post_id=request.form.get("post_id"),
            author_id=request.form.get("author_id")
        )

        db.session.add(new_comment)
        db.session.commit()

        comment_dict = new_comment.to_dict()

        return make_response(jsonify(comment_dict), 200)


@app.route("/comments/<int:id>", methods=["GET", "PATCH", "DELETE"])
def comment_by_id(id):
    comment = Comment.query.filter_by(id=id).first()

    if request.method == "GET":
        comment_dict = comment.to_dict()

        return make_response(jsonify(comment_dict), 200)

    elif request.method == "PATCH":
        for attr in request.form:
            setattr(comment, attr, request.form.get("attr"))

            db.session.add(comment)
            db.session.commit()

            comment_dict = comment.to_dict()

            return make_response(jsonify(comment_dict), 200)

    elif request.method == "DELETE":
        db.session.delete(comment)
        db.session.commit()

        return make_response([
            "comment deleted"
        ], 201)


@app.route("/authors", methods=["GET", "POST"])
def authors():
    if request.method == "GET":
        authors = [author.to_dict() for author in Author.query.all()]
        return make_response(jsonify(authors), 200)

    elif request.method == "POST":
        new_author = Author(
            username=request.form.get("username"),
            email=request.form.get("email")
        )

        db.session.add(new_author)
        db.session.commit()

        author_dict = new_author.to_dict()

        return make_response(jsonify(author_dict), 200)


@app.route("/authors/<int:id>", methods=["GET", "PATCH", "DELETE"])
def authors_by_id(id):
    author = Author.query.filter_by(id=id).first()

    if request.method == "GET":
        author_dict = author.to_dict()

        return make_response(jsonify(author_dict), 200)

    elif request.method == "PATCH":
        for attr in request.form:
            setattr(author, attr, request.form.get(attr))
            db.session.add(author)
            db.session.commit()

            author_dict = author.to_dict()

            return make_response(jsonify(author_dict), 200)

    elif request.method == 'DELETE':
        db.session.delete(author)
        db.session.commit()

        return make_response([
            "Author has been deleted", 2
        ])


if __name__ == "__main__":
    app.run(port=5555, debug=True)
