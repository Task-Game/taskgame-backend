from flask import Blueprint, make_response, request, jsonify
from .Tarefa import Tarefa
import json
task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/api/v1.0/tasks', methods=['GET'])
def index():
    response = Tarefa.index()

    return response, Response(status=200)


@task_bp.route('/api/v1.0/tasks', methods=['POST'])
def create():
    """
    Rota responsavel por criar novas tasks no banco
    """
    

@task_bp.route('/api/v1.0/tasks/<idTask>', methods=['GET'])
def show(idTask):
    request_json = request.get_json()

    idTask = request_json['data']['idTask']

    task = Tarefa.show(idTask)

    return task, Response(status=200)

@task_bp.route('/api/v1.0/tasks/<idTask>', methods=['PUT'])
def upgrade(idTask):
    request_json = request.get_json()

    idTask = request_json['data']['idTask']
    # get another request body data here

    task = Tarefa.upgrade(idTask)

    return task, Response(status=200)


@task_bp.route('/api/v1.0/tasks/<idTask>', methods=['DELETE'])
def destroy(idTask):
    request_json = request.get_json()

    idTask = request_json['data']['idTask']

    task = Tarefa.destroy(idTask)

    return task, Response(status=200)

@task_bp.route('/api/v1.0/tasks/<idTask>/users_in_task', methods=['GET'])
def users_in_task(idTask):
    request_json = request.get_json()

    idTask = request_json['data']['idTask']

    task = Tarefa.userInTask(idTask)

    return task, Response(status=200)
