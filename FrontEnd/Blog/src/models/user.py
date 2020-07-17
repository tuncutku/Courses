from database import db


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = _id

    @classmethod
    def get_by_id(cls):
        pass

    @classmethod
    def get_by_email(cls):
        pass

    @staticmethod
    def login_valid(email, password):
        pass

    @staticmethod
    def register(email, password):
        pass

    def login():
        pass

    def logout():
        pass

    def get_blogs():
        pass

    def json(self):
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password,
        }

    @classmethod
    def register(cls, email, password):
        user = cls(email, password)
        db.add_user(user)

