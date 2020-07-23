from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_namespace
from .main.controller.task_controller import api as task_namespace
from .main.controller.group_controller import api as group_namespace
from .main.controller.item_controller import api as item_namespace


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title="TaskGame Backend flask RestAPI",
          version='1.0',
          description='Api criada com o intuito de ser o backend da aplicacão "TaskGame" - TCC Desenvolvimento de Sistema ETEC Irmã Agostina'
          )

api.add_namespace(user_namespace, path='/api/v1/user')
api.add_namespace(task_namespace, path='/api/v1/task')
api.add_namespace(group_namespace, path='/api/v1/group')
api.add_namespace(item_namespace, path='/api/v1/item')
