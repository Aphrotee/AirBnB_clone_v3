#!/usr/bin/python3

"""
contains route methods
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {
           'users': User, 'places': Place,
           'states': State, 'cities': City, 'amenities': Amenity,
           'reviews': Review
          }


@app_views.route('/states/<state_id>/cities', strict_slashes=False)
def get_cities(state_id):
    cities = storage.all(City)
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    cities_js = [city.to_dict() for city in cities.values()\
            if city.state_id == state_id]
if __name__ == '__name__':
    pass
