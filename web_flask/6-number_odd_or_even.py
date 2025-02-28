#!/usr/bin/python3
""" script that starts a Flask web application"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>')
def python(text):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def IsAnInt(n):
    if type(n) is int:
        return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def IsAnIntv2(n):
    if type(n) is int:
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def IsAnIntv3(n):
    if type(n) is int:
        return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
