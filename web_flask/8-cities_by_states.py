#!/usr/bin/python3
"""stating a simple flask web app"""
from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def staties():
    states = []
    for state in storage.all(State).values():
        states.append(state)
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
