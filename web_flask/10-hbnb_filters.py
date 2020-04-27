#!/usr/bin/python3
"""stating a simple flask web app"""
from flask import Flask, render_template
from models import storage, State, Amenity
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def staty():
    states = []
    for state in storage.all(State).values():
        states.append(state)
    amenities = []
    for amenity in storage.all(Amenity).values():
        amenities.append(amenity)
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
