from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_namespace

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title="TaskGame Backend flask RestAPI",
          version='1.0',
          description='Api criada com o intuito de ser o backend da aplicacão "TaskGame" - TCC Desenvolvimento de Sistema ETEC Irmã Agostina'
          )

api.add_namespace(user_namespace, path='/user')
