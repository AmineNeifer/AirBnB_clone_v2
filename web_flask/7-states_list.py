#!/usr/bin/python3
"""stating a simple flask web app"""
from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def staties():
    states = storage.all(State)
    first = {}
    last = {}
    for value in states.values():
        first[value.to_dict()["name"]] = value.to_dict()["id"]
    for key, value in sorted(first.items()):
        last[key] = value
    del first
    return render_template("7-states_list.html", all_states=last)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
