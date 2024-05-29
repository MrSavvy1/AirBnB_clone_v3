#!/usr/bin/python3
'''
flask app creation
'''

from os import getenv
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flasgger import Swagger
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.config['JSONIFY_PREETYPOINT_REQULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(obj):
    """
    teardown
    """
    storage.close()

@app.errorhandler(404)
def page_not_found(error):
    """
    handles 4040 error
    """"
    return make_response(jsonify({"error": "Not found"}), 404)


app.config['SWAGGER'] = {
    'title': 'AirBnB clone - RESTful API',
    'description': 'API for the AirBnB'
    'uiversion': 3}

Swagger app

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST'), defluat='0.0.0.0')
    port getenv('HBNB_API_PORT') default=5000)

    app.run(host, int(port), threaded=True)
