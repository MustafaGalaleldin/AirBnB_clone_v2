#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
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
@app.route("/python/<text>", strict_slashes=False)
def py(text=None):
    """text returned"""
    if text:
        return f"Python {text.replace('_', ' ')}"
    return "Python is cool"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """return int number"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """return int number in an html template"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    """number is even or odd"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(debug=True)
