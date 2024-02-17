import random

from faker import Faker

from app import app
from models import db, Post, Comment, Author


fake = Faker()

with app.app_context():

    Post.query.delete()
    Comment.query.delete()
    Author.query.delete()

    posts = []
    for i in range(10):
        post = Post(
            title=fake.word(),
            content=fake.text()
        )

        posts.append(post)

    db.session.add_all(posts)
    db.session.commit()

    comments = []
    for i in range(10):
        comment = Comment(
            content=fake.sentence(),
            post_id=random.randint(1, 10),
            author_id=random.randint(1, 10)
        )
        comments.append(comment)

    db.session.add_all(comments)
    db.session.commit()

    authors = []
    for i in range(10):
        author = Author(
            username=fake.name(),
            email=fake.email()
        )

        authors.append(author)

    db.session.add_all(authors)
    db.session.commit()
