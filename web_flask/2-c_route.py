#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Displays Hello HBHB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index_2():
    """Displays HBHB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def index_3(text):
    """Displays value of the text variable"""
    return 'C ' + str(text.replace("_", " "))


if __name__ == '__main__':
    """Entry Point"""
    app.run(host='0.0.0.0', port=5000)
