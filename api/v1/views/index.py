#!/usr/bin/python3
'''
app views
'''

from flask import jsonify
from api.v1.views import app_views

from models import storage

@app_views.route("/status", methods=['GET', strict_slashes=False)
def status():
    """
    app def
    """
    data = {
	"status": "OK"
    }

    resp = jsonify
    res.status_code = 200


    return resp

@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def stats():
    """
    stats of obj
    """
    data = {
	"amenities": storage.count("Amenity"),
	"cities": storage.count("City"),
	"places": storage.count("Places"),
	"users": storage.count("Users"),
	"states": storage.count("States"),
	"reviews": storage.count("User")
    }

    resp = jsonify(data)
    resp.status_code = 200

    return resp
