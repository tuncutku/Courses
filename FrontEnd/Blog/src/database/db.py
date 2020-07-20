from database.connection import get_cursor

CREATE_USERS = "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, email TEXT, password TEXT);"
CREATE_POSTS = """
CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY, 
    blog_id INTEGER, 
    title TEXT, 
    content TEXT, 
    author TEXT, 
    date DATE, 
    FOREIGN KEY(blog_id) REFERENCES blogs(id)
    );"""
CREATE_BLOGS = """
CREATE TABLE IF NOT EXISTS blogs (
    id SERIAL PRIMARY KEY, 
    description TEXT,
    author TEXT, 
    author_id INTEGER, 
    FOREIGN KEY(author_id) REFERENCES users(id)
    );"""

INSERT_USER = "INSERT INTO users (email, password) VALUES (%s, %s);"
INSERT_BLOG = (
    "INSERT INTO blogs (author, title, description, author_id) VALUES (%s,%s,%s,%s);"
)
INSERT_POST = (
    "INSERT INTO posts (blog_id, title, content, author, date) VALUES (%s,%s,%s,%s,%s);"
)
SELECT_USER_BY_EMAIL = "SELECT email, password, id FROM users WHERE email = %s;"
SELECT_USER_BY_ID = "SELECT email, password, id FROM users WHERE id = %s;"
SELECT_BLOGS_BY_AUTHOR_ID = (
    "SELECT author, title, description, author_id, id FROM blogs WHERE author_id = %s;"
)
SELECT_BLOG_BY_ID = (
    "SELECT author, title, description, author_id, id FROM blogs WHERE id = %s;"
)
SELECT_POSTS_BY_BLOG_ID = (
    "SELECT blog_id, title, content, author, date FROM posts WHERE  blog_id = %s"
)


def create_tables(connection):
    with get_cursor(connection) as cursor:
        cursor.execute(CREATE_USERS)
        cursor.execute(CREATE_BLOGS)
        cursor.execute(CREATE_POSTS)


# -- blogs --


def find_blog_by_author_id(author_id):
    with get_cursor() as cursor:
        cursor.execute(SELECT_BLOGS_BY_AUTHOR_ID, (author_id,))
        return cursor.fetchall()


def get_blog_by_id(blog_id):
    with get_cursor() as cursor:
        cursor.execute(SELECT_BLOG_BY_ID, (blog_id,))
        return cursor.fetchone()


def add_blog(author, title, description, author_id):
    with get_cursor() as cursor:
        cursor.execute(INSERT_BLOG, (author, title, description, author_id))


# -- posts --


def get_posts_by_blog_id(blog_id):
    with get_cursor() as cursor:
        cursor.execute(SELECT_POSTS_BY_BLOG_ID, (blog_id,))
        return cursor.fetchall()


def add_post(blog_id, title, content, author, date):
    with get_cursor() as cursor:
        cursor.execute(INSERT_POST, (blog_id, title, content, author, date))


# -- users --


def add_user(email, password):
    with get_cursor() as cursor:
        cursor.execute(INSERT_USER, (email, password))


def find_user_by_email(email):
    with get_cursor() as cursor:
        cursor.execute(SELECT_USER_BY_EMAIL, (email,))
        return cursor.fetchone()


def find_user_by_id(_id):
    with get_cursor() as cursor:
        cursor.execute(SELECT_USER_BY_ID, (_id,))
        return cursor.fetchone()
