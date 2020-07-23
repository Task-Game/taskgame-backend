from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from .config import config_by_name, BaseConfig

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

def create_app(config_name):
    """
        Cria a instancia do app flask com todas as configurações
    """
    app = Flask(__name__)

    """ Cors settings will be here. We maybe use this endpoint later. """
    cors = CORS(app, resources={
        r"/*": {
            'origins': "*"
        }
    })

    app.config.from_object(config_by_name['development'])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    
    return app