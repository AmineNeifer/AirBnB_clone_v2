#!/usr/bin/python3
"""stating a simple flask web app"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
