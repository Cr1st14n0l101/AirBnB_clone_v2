#!/usr/bin/python3
"""Simple Flask app, with additional route"""
from flask import Flask, abort, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_holberton():
    """Hello Flask"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    """hello holberton"""
    return 'HBNB'


@app.route('/c/<text>')
def run_text(text):
    """Run text"""
    text = 'C ' + text.replace('_', ' ')
    return text


@app.route('/python/<text>')
@app.route('/python')
def run_python(text='is cool'):
    """Python route"""
    text = 'Python ' + text.replace('_', ' ')
    return text


@app.route('/number/<n>')
def run_number(n):
    """Run number"""
    try:
        n = int(n)
    except ValueError:
        abort(404)
    text = str(n) + ' is a number'
    return text


@app.route('/number_template/<n>')
def run_template(n):
    """Template example"""
    try:
        n = int(n)
    except ValueError:
        abort(404)
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<n>')
def run_template_odd_or_even(n):
    """Odd or even"""
    try:
        n = int(n)
    except ValueError:
        abort(404)
    t = 'odd'
    if n % 2 == 0:
        t = 'even'
    return render_template('6-number_odd_or_even.html', n=n, t=t)


@app.route('/states_list')
def run_all_states():
    """Run all states"""
    list = storage.all('State')
    return render_template('7-states_list.html', storage=list)


@app.teardown_appcontext
def do_teardown(self):
    """Closes session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
