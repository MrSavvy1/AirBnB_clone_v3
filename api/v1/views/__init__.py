#!/usr/bin/python3
'''
create the app
'''
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='api/v1/')

from app.v1.views.index import *
from app.v1.views.places import *
from app.v1.views.states import *
from app.v1.views.users import *
from app.v1.views.amenities import *
from app.v1.views.cities import *
