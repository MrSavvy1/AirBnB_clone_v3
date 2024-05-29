#!/usr/bin/python3
'''
app views
'''
from flask import Flask
from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status', strict_slashes=False)
def status():
    """
    app def
    """
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def count():
    """
    stats number of obj
    """
    return jsonify({"amenities": storage.count("Amenity"),
	"cities": storage.count("City"),
	"places": storage.count("Places"),
	"users": storage.count("Users"),
	"states": storage.count("States"),
	"reviews": storage.count("User")
    })
