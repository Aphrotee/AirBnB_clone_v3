#!/usr/bin/python3

"""
This is a flask app that has an endpoint (route)
that will return the status of your API.
"""


from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(anException):
    """closes storage"""
    storage.close()


@app.errorhandler(404)
def error_404(e):
    """returns JSON resonse for 404 error"""
    error = {'error': 'Not found'}
    return jsonify(error), 404


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)
