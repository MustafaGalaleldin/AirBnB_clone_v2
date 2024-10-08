#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.teardown_appcontext
def tear(exception):
    "tear down"
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    " display a HTML states page"
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
