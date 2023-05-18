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


@app.route("/c/<text>")
def display_c(text):
    """
    Route to display “C ” followed by the value of the text
    """
    result = "C " + text.replace("_", " ")
    return result


@app.route('/python/')
@app.route("/python/<text>")
def display_python(text="is cool"):
    """
    Route to display “Python ” followed by the value of the text
    """
    result = "Python " + text.replace("_", " ")
    return result


@app.route("/number/<int:n>")
def display_n(n):
    """
    Route to display “n is a number” only if n is an integer
    """
    result = "{:d} is a number".format(n)
    return result


@app.route("/number_template/<int:n>")
def display_n_template(n):
    """
    Route to display a HTML page only if n is an integer
    """
    result = "{:d} is a number".format(n)
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """
    Route to display a HTML page only if n is an intege
    """
    if n % 2 == 0:
        result = "is even"
    else:
        result = "is odd"
    return render_template("6-number_odd_or_even.html",
                           number=n,
                           result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
