from datetime import datetime

from models.post import Post
from database import db


class Blog(object):
    def __init__(self, auther, title, description, author_id, _id=None):
        self.id = _id
        self.author = auther
        self.title = title
        self.description = description
        self.author_id = author_id

    def new_post(self):
        title = input()
        content = input()
        date = input()
        post = Post(
            self.id, title, content, self.author, datetime.strptime(date, "%d%m%Y")
        )
        post.save()

    def get_posts(self):
        return Post.get_post_list(self.id)

    def save_blog(self):
        db.add_blog(self.author, self.title, self.description, self.author_id)

    @classmethod
    def get_blogs(cls, author_id):
        blogs = db.find_blog_by_author_id(author_id)
        return [cls(*blog) for blog in blogs]

    @classmethod
    def get_blog(cls, blog_id):
        blog = db.get_blog_by_id(blog_id)
        return cls(*blog)
