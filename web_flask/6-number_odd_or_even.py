#!/usr/bin/python3
"""stating a simple flask web app"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C %s' % text.replace("_", " ")


@app.route('/python', strict_slashes=False)
def only_python():
    return 'Python is cool'


@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return 'Python %s' % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    if (n % 2 == 0):
        return render_template('6-number_odd_or_even.html', n=n, what="even")
    return render_template('6-number_odd_or_even.html', n=n, what="odd")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
