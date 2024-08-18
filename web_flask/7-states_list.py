#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models import City
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    " display a HTML states page"
    states = sorted(list(storage.all(State).values()), key=lambda st: st.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tear(exception):
    "tear down"
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
