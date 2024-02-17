from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Post(db.Model, SerializerMixin):
    __tablename__ = "posts"

    serialize_rules = ("-comments.post",)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)

    comments = db.relationship("Comment", back_populates="post")


class Comment(db.Model, SerializerMixin):
    __tablename__ = "comments"

    serialize_rules = ("-author.comments", "-post.comments",)

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)

    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))

    post = db.relationship("Post", back_populates="comments")
    author = db.relationship("Author", back_populates="comments")


class Author(db.Model, SerializerMixin):
    __tablename__ = "authors"

    serialize_rules = ("-comments.author",)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)

    comments = db.relationship("Comment", back_populates="author")
