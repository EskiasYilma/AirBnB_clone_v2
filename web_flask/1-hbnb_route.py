#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """
    Route to display “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def display_HBNB():
    """
    Route to display “HBNB!”
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
