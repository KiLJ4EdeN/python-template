"""Main App."""
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)


# root
@app.route("/")
def index():
    """Send Hello World Back to User.

    Returns:
        json: Hello World As Key Value Pair In JSON Format
    """
    return jsonify({"hello": "world"})


# coverage index
@app.route("/cov/")
def send_cov_index():
    """Send Index Route For Coverage.

    Returns:
        html: index.html
    """
    return send_from_directory("../coverage", "index.html")


# coverage
@app.route("/cov/<path:path>")
def send_cov(path: str):
    """Send Coverage Static Files.

    Args:
        path (str): Path to Coverage Dir Html File
    Returns:
        html: Html File
    """
    return send_from_directory("../coverage", path)


# docs index
@app.route("/docs/")
def send_doc_index():
    """Send Index Route For Documentation.

    Returns:
        html: index.html
    """
    return send_from_directory("../docs/build/html", "index.html")


# docs
@app.route("/docs/<path:path>")
def send_doc(path: str):
    """Send Documentation Static Files.

    Args:
        path (str): Path to Documentation Dir Html File
    Returns:
        html: Html File
    """
    return send_from_directory("../docs/build/html", path)


if __name__ == "__main__":
    app.run()
