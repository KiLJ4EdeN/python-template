"""Main App."""
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)


# root
@app.route("/")
def index():
    """_summary_.

    Send Hello World Back to User.
    Returns:
        _type_: _description_
        Hello World As Key Value Pair In JSON Format
    """
    return jsonify({"hello": "world"})


# coverage index
@app.route("/cov/")
def send_cov_index():
    """_summary_.

    Send Index Route For Coverage.
    Returns:
        _type_: _description_
        index.html
    """
    return send_from_directory("../coverage", "index.html")


# coverage
@app.route("/cov/<path:path>")
def send_cov(path):
    """_summary_.

    Send Coverage Static Files.
    Args:
        path (_type_): _description_
    Path to Coverage Dir Html File
    Returns:
        _type_: _description_
        Html File
    """
    return send_from_directory("../coverage", path)


# docs index
@app.route("/docs/")
def send_doc_index():
    """_summary_.

    Send Index Route For Documentation.
    Returns:
        _type_: _description_
        index.html
    """
    return send_from_directory("../docs/build/html", "index.html")


# docs
@app.route("/docs/<path:path>")
def send_doc(path):
    """_summary_.

    Send Documentation Static Files.
    Args:
        path (_type_): _description_
    Path to Documentation Dir Html File
    Returns:
        _type_: _description_
        Html File
    """
    return send_from_directory("../docs/build/html", path)


if __name__ == "__main__":
    app.run()
