#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """return phrase"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display “HBNB”"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """variables"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
def py():
    """text returned"""
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def py2(text):
    """text returned"""
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(debug=True)
