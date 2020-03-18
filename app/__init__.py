from flask import Flask
from flask_cors import CORS

from config import BaseConfig
from config import configure_app

from .api.Usuario import usuario_routes
from .api.Tarefa import tarefa_routes
from .api.Projeto import projeto_routes
from .api.Metas import metas_router
from .api.Item import item_routes
from .api.Loja import loja_routes

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


    app.register_blueprint(usuario_routes.user_bp)
    app.register_blueprint(tarefa_routes.task_bp)
    app.register_blueprint(projeto_routes.project_bp)
    app.register_blueprint(metas_routes.goals_bp)
    app.register_blueprint(item_routes.item_bp)
    app.register_blueprint(loja_routes.shop_bp)

    return app