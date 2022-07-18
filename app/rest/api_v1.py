import logging

from flask import Blueprint
from flask_restx import Api

from app.rest.v1.citybike_rest import citybike_ns

_log = logging.getLogger(__name__)

api_v1 = Blueprint("api_v1", __name__, url_prefix="/imobility/v1")
api = Api(api_v1, doc="/api/doc", version="1.0", title="iMobility2 API Version 1")

api.add_namespace(citybike_ns)
