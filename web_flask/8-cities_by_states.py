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
    states = storage.all(State)
    it_state = 0
    last = []
    for state in states.values():
        last.append([[state.to_dict()["id"], state.to_dict()["name"]]])
        for city in state.cities:
            cit = city.to_dict()
            last[it_state].append([cit["id"], cit["name"]])
        it_state += 1

    return render_template("8-cities_by_states.html", all_states=last)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
