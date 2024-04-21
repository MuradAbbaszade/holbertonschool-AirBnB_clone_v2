#!/usr/bin/python3
"""Flask Project"""
from models.__init__ import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def display_states():
    states = storage.all(State).values()
    new_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', objs=new_states)


@app.route("/states/<state_id>", strict_slashes=False)
def display_state_by_id(state_id):
    states = storage.all(State).values()
    state = list(filter(lambda x: x.id == state_id, states))
    return render_template("9-states.html", objs=state)


@app.route("/cities_by_states", strict_slashes=False)
def display_cities_by_states():
    states = storage.all(State).values()
    new_states = sorted(states, key=lambda x: x.name)
    return render_template('8-cities_by_states.html', objs=new_states)


@app.teardown_appcontext
def close_db(exc):
    storage.close()


if __name__ == "__main__":
    app.run()
