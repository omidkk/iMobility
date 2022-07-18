import logging

from flask_restx import Namespace, Resource, cors

from app.services.citybike_service import CityBikeService

_log = logging.getLogger(__name__)

citybike_ns = Namespace(
    "citybike", description="Citybike related operations", decorators=[cors.crossdomain(origin="*")],
)


@citybike_ns.route("/")
class CityBikeListRest(Resource):
    def get(self):
        try:
            result = CityBikeService.get()

            return result, 200, {"content-type": "application/json"}

        except Exception as e:
            _log.warning(e)
            return {"message": str(e)}, 500, {"content-type": "application/json"}
