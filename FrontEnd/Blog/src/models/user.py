from flask import session
from database import db
from models.blog import Blog


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = _id

    @classmethod
    def get_by_id(cls, _id):
        data = db.find_user_by_id(_id)
        if data is not None:
            return cls(*data)      

    @classmethod
    def get_by_email(cls, email):
        data = db.find_user_by_email(email)
        if data is not None:
            return cls(*data)

    @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email)
        if user is not None:
            # Check the password
            return user.password == password
        return False

    @staticmethod
    def login(user_email):
        # login_valid has already been called
        session["email"] = user_email

    def logout():
        pass

    def get_blogs(self):
        return Blog.get_blogs(self._id)

    def json(self):
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password,
        }

    @staticmethod
    def register(email, password):
        db.add_user(email, password)

