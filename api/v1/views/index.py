#!/usr/bin/python3

"""
contains route methods
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status_endpoint():
    status_msg = {
                    'status': 'OK'
                }
    return jsonify(status_msg)

if __name__ == '__name__':
    pass
