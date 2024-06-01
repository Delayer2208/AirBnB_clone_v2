#!/usr/bin/python3
"""
Start a Flask web application with integer template rendering
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a simple greeting."""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB string."""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Return 'C ' followed by the value of the text variable."""
    return 'C ' + text.replace('_', ' ')

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Return 'Python ' followed by the value of the text variable."""
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Return 'n is a number' only if n is an integer."""
    return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Render a template only if n is an integer."""
    return render_template('5-number.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
