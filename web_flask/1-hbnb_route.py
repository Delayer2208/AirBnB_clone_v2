#!/usr/bin/python3
"""
A Flask application with multiple routes
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def welcome():
    """Returns a greeting."""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Returns HBNB string."""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
