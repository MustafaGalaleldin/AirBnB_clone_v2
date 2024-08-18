#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.teardown_appcontext
def tear(exception=None):
    "tear down"
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    "show states"
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_city(id):
    "show cities with state_id"
    existed = False
    st_cities = None
    st_state = None
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            existed = True
            st_state = state
            break
    return render_template('9-states.html',
                           existed=existed,
                           state=st_state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
