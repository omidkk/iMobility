"""Initialize Flask app."""
import logging

from flask import Flask

from app.config import Config
from app.rest.api_v1 import api_v1

_log = logging.getLogger(__name__)


def create_app():

    _log.info("start create the app.")

    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object(Config)

    app.register_blueprint(api_v1)

    return app
