from datetime import datetime


class Post(object):
    def __init__(
        self, blog_id, title, content, author, date=datetime.datetime.utcnow(), _id=None
    ):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self._id = _id

    def json(self):
        return {
            "id": self._id,
            "blog_id": self.blog_id,
            "author": self.author,
            "content": self.content,
            "title": self.title,
            "created_date": self.created_date,
        }

    def save(self):
        pass

    @classmethod
    def get_post_with_id(cls):
        pass

    def get_post_with_blog(self):
        pass

    def get_post_list(self):
        pass

    def new_post(self):
        pass
