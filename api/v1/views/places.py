#!/usr/bin/python3
"""
route for place
"""
from api.v1.views import app_views, storage
from flask import jsonify, abort, request
from models.place import Place

@app_views.route("/cities/<city_id>/places", methods=["GET"],
		strict_slashes=False)
def places_by_city(city_id):
    """
    retrieve place object
    """
    place_list = []
    city_obj = storage.get("City", str(city_id))
    for obj in city_obj.places:
	place_list.apend(obj.to_json())

    return


@app.views.route("/places/<place_id>", methods=["GET"],
		strict_slashes=False)
def place_by_id(place_id):
    """
    get by id
    """
    fetch = storage.get("Place", str(place_id))

    if fetch is None:
	abort(404)

    return jsonify(fetch.to_json())
