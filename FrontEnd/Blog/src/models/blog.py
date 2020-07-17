from models.post import Post
from datetime import datetime


class Blog(object):
    def __init__(self, auther, title, description, author_id, _id=None):
        self.id = _id
        self.auther = auther
        self.title = title
        self.description = description
        self.auther_id = author_id

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

    def save(self):
        pass

    def json(self):
        pass

    @classmethod
    def get_blog(cls, id):
        pass

    def new_blog(self, title, description):
        pass
