# Route converters pass the captured URL components to the view functions.
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello():
    return "Home page"


@app.route("/tuna")
def tuna():
    return "<h2>Tuna is good</h2>"


@app.route("/user/<username>")
def show_user_profile(username):
    return "Hey there %s" % escape(username)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post id: %d" % post_id


if __name__ == "__main__":
    app.run()
