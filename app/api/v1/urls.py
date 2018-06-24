from flask import Blueprint
from app.api.v1.demo_api import demo_api

api_v1 = Blueprint('api.v1', __name__)

api_v1.add_url_rule('/demo-api/', view_func=demo_api)