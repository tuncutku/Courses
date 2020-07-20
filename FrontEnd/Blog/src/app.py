from flask import Flask, render_template, request, session, make_response
from flask_restful import Api

from models.user import User
from models.blog import Blog
from models.post import Post

__author__ = "tuncutku"

app = Flask(__name__)
app.secret_key = "tunc"
api = Api(app)


@app.route("/")
def home_template():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/auth/register", methods=["POST", "GET"])
def auth_register():
    email = request.form["email"]
    password = request.form["password"]
    User.register(email, password)
    session["email"] = password
    return render_template("profile.html", email=session["email"])


@app.route("/auth/login", methods=["POST", "GET"])
def auth_login():
    email = request.form["email"]
    password = request.form["password"]
    if User.login_valid(email, password):
        User.login(email)
    else:
        session["email"] = None

    return render_template("profile.html", email=session["email"])


@app.route("/blogs/<string:user_id>")
@app.route("/blogs")
def blogs(user_id=None):
    if user_id is not None:
        user = User.get_by_id(user_id)
    else:
        user = User.get_by_email(session["email"])
    blogs = user.get_blogs()

    return render_template("user_blogs.html", blogs=blogs, email=user.email)


@app.route("/posts/<string:blog_id>", methods=["POST", "GET"])
def posts(blog_id):
    blog = Blog.get_blog(blog_id)
    posts = blog.get_posts()

    return render_template(
        "posts.html", posts=posts, blog_title=blog.title, blog_id=blog.id
    )


@app.route("/blogs/new", methods=["POST", "GET"])
def create_new_blog():
    if request.method == "GET":
        return render_template("new_blog.html")
    else:
        title = request.form["title"]
        description = request.form["description"]
        user = User.get_by_email(session["email"])

        new_blog = Blog(user.email, title, description, user._id)
        new_blog.save_blog()

        return make_response(blogs(user._id))


@app.route("/posts/new/<string:blog_id>", methods=["POST", "GET"])
def create_new_post(blog_id):
    if request.method == "GET":
        return render_template("new_post.html", blog_id=blog_id)
    else:
        title = request.form["title"]
        content = request.form["content"]
        user = User.get_by_email(session["email"])

        new_post = Post(blog_id, title, content, user.email)
        new_post.save_post()

        return make_response(posts(blog_id))


if __name__ == "__main__":
    # create_tables()
    app.run(port=5000, debug=True)
