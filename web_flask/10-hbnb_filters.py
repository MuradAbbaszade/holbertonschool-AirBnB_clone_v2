#!/usr/bin/python3
"""Flask Project"""
from models.__init__ import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def display_filters():
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    new_states = sorted(states, key=lambda x: x.name)
    new_amenities = sorted(amenities, key=lambda x: x.name)
    return render_template('10-hbnb_filters.html', states=new_states, amenities=new_amenities)



@app.teardown_appcontext
def close_db(exc):
    storage.close()


if __name__ == "__main__":
    app.run()
