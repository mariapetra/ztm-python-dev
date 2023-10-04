from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


@app.route("/<username>/<int:post_id>")
def hello_world(username=None, post_id=None):
    return render_template("index.html", name=username, post_id=post_id)


@app.route("/about")
def about():
    return render_template("about.html")


# @app.route("/favicon.ico")
# def favicon():
#     return send_from_directory(
#         os.path.join(app.root_path, "static"),
#         "favicon.ico",
#         mimetype="favicon.ico",
#     )
