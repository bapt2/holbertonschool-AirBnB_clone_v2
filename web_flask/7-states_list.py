#!/usr/bin/python3
""" script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
@app.route('/states_list', strict_slashes=False)
def ListOfStates(States):
    render_template('7-states_list.html', States=States)
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
