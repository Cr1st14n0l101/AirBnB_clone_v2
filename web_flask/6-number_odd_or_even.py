#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
from flask import render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def index_4(text='is cool'):
    """Displays value of the text variable, text now have a default value"""
    return 'Python ' + str(text.replace("_", " "))


@app.route('/number/<n>', strict_slashes=False)
def index_5(n):
    """Displays value of the n variable if is integer"""
    if type(int(n)) == int:
        return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def index_6(n):
    """Displays a html file with the n variable if is integer"""
    return render_template('/5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def index_7(n):
    """Displays a html file with the n variable if is integer"""
    if n % 2 == 0:
        return render_template('/6-number_odd_or_even.html', n=n, m='even')
    else:
        return render_template('/6-number_odd_or_even.html', n=n, m='odd')


if __name__ == '__main__':
    """Entry Point"""
    app.run(host='0.0.0.0', port=5000)
