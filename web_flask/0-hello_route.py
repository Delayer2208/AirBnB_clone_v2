#!/usr/bin/python3
"""
A Flask application to start a simple web server
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def welcome():
    """Returns a greeting."""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
