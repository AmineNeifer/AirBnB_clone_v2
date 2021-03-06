#!/usr/bin/python3
"""stating a simple flask web app"""
from flask import Flask
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


if __name__ == "__main__":
    app.run(host='0.0.0.0')
