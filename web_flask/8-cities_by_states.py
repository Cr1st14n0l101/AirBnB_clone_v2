#!/usr/bin/python3
"""Script that starts a Flask web application"""
from models import storage
from models.state import State
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


@app.teardown_appcontext
def index_8(self):
    """Close the ssesion"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def index_9():
    """Display a HTML page with a storage"""
    return render_template('/7-states_list.html',
                           storage=storage.all(State))


@app.route('/cities_by_states', strict_slashes=False)
def index_10():
    """Display a HTML page with a storage"""
    return render_template('/8-cities_by_states.html',
                           storage=storage.all(State))


if __name__ == '__main__':
    """Entry Point"""
    app.run(host='0.0.0.0', port=5000)
