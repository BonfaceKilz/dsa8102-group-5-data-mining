"""Entry point from spinning up flask"""
import os

from server.general import general

from typing import Dict
from typing import Union
from flask import Flask


def create_app(config: Union[Dict, str, None] = None) -> Flask:
    """Create a new flask object"""
    app = Flask(__name__)
    # Load default configuration
    app.config.from_object("server.settings")

    # Load environment configuration
    if "NEWSFEED_CONF" in os.environ:
        app.config.from_envvar('NEWSFEED_CONF')

    # Load app specified configuration
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith(".py"):
            app.config.from_pyfile(config)

    app.register_blueprint(general, url_prefix="/")

    return app
