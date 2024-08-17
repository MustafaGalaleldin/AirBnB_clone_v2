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


@app.route('/cities_by_states', strict_slashes=False)
def cities():
    "show cities by states"
    states = sorted(list(storage.all(State).values()), key=lambda st: st.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
