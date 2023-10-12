from flask import Flask, render_template, send_from_directory, url_for

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:pag_name>")
def html_page(page_name):
    return render_template(page_name)

# @app.route("/submit_form" methods=['POST', 'GET'])
# def submit_form():
#     retr