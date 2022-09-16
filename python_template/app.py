"""Main App."""
import os

from dotenv import load_dotenv
from flask import Flask, Response, jsonify, send_from_directory

# load .env
load_dotenv()
app = Flask(__name__)
APP_PORT = int(os.getenv("APP_PORT", "5000"))


# root
@app.route("/")
def index() -> Response:
    """Send Hello World Back to User.

    Returns:
        json: Hello World As Key Value Pair In JSON Format
    """
    return jsonify({"hello": "world"})


# coverage index
@app.route("/cov/")
def send_cov_index() -> Response:
    """Send Index Route For Coverage.

    Returns:
        html: index.html
    """
    return send_from_directory("../coverage", "index.html")


# coverage
@app.route("/cov/<path:path>")
def send_cov(path: str) -> Response:
    """Send Coverage Static Files.

    Args:
        path (str): Path to Coverage Dir Html File
    Returns:
        html: Html File
    """
    return send_from_directory("../coverage", path)


# docs index
@app.route("/docs/")
def send_doc_index() -> Response:
    """Send Index Route For Documentation.

    Returns:
        html: index.html
    """
    return send_from_directory("../site", "index.html")


# docs
@app.route("/docs/<path:path>")
def send_doc(path: str) -> Response:
    """Send Documentation Static Files.

    Args:
        path (str): Path to Documentation Dir Html File
    Returns:
        html: Html File
    """
    ext_list = [".png", ".js", ".css", ".min"]
    if not any([ext in path for ext in ext_list]):
        path = path + "/" + "index.html"
        return send_from_directory("../site", path)
    else:
        return send_from_directory("../site", path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT)
