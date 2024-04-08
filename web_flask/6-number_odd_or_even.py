#!user/bin/python3
from flask import Flask, render_template
"""This script starts a Flask web application"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


""" Display “C ” followed by the value of the text variable (replace underscore _ symbols with a space ) """

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C %s' % text.replace('_', ' ')

"""Display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )"""

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    return 'Python %s' % text.replace('_', ' ')

"""Display a number only if it is an integer"""

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '%d is a number' % n

"""Display a HTML page only if n is an integer"""

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)

"""Display a HTML page only if n is an integer and is odd or even"""

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
