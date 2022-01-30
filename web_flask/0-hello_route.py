#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Displays Hello HBHB!"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    """Entry Point"""
    app.run(host='0.0.0.0', port=5000)
