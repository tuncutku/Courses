from database.connection import get_cursor

CREATE_USERS = "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, email TEXT, password TEXT);"
CREATE_POSTS = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY, 
    blog_id INTEGER, 
    title TEXT, 
    content TEXT, 
    author TEXT, 
    date DATE, 
    FOREIGN KEY(blog_id) REFERENCES blogs(id)
    );"""
CREATE_BLOGS = """
CREATE TABLE IF NOT EXISTS blogs (
    id INTEGER PRIMARY KEY, 
    description TEXT,
    author TEXT, 
    author_id INTEGER, 
    FOREIGN KEY(author_id) REFERENCES users(id)
    );"""

INSERT_USER = "INSERT INTO users (email, password) VALUES (%s, %s)"
SELECT_USER_BY_EMAIL = "SELECT email, password FROM users WHERE email = %s"


def create_tables(connection):
    with get_cursor(connection) as cursor:
        cursor.execute(CREATE_USERS)
        cursor.execute(CREATE_BLOGS)
        cursor.execute(CREATE_POSTS)


# -- blogs --


# -- posts --


# -- users --


def add_user(email, password):
    with get_cursor() as cursor:
        cursor.execute(INSERT_USER, (email, password))


def find_user_by_email(email):
    with get_cursor() as cursor:
        cursor.execute(SELECT_USER_BY_EMAIL, (email,))
        return cursor.fetchone()
