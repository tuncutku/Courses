from datetime import datetime
from database import db


class Post(object):
    def __init__(
        self, blog_id, title, content, author, date=datetime.utcnow(), _id=None
    ):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self._id = _id

    @classmethod
    def get_post_list(cls, blog_id):
        posts = db.get_posts_by_blog_id(blog_id)
        return [cls(*post) for post in posts]

    def save_post(self):
        db.add_post(self.blog_id, self.title, self.content, self.author, self.date)

