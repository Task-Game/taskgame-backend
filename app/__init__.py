from flask import Flask
from flask_cors import CORS

from config import BaseConfig
from config import configure_app

def create_app():
    app = Flask(__name__)

    """ Cors settings will be here. We maybe use this endpoint later. """
    cors = CORS(app, resources={
        r'/api/*': {
            'origins': BaseConfig.ORIGINS
        }
    })

    configure_app(app)
    app.url_map.strict_slashes = False

    # app.register_blueprint(user, url_prefix='/api/users')

    return app