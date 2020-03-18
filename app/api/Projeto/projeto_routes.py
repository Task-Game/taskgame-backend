from flask import Blueprint, request, Response
from .Projeto import Projeto
import json
project_bp = Blueprint('project_bp', __name__)


@project_bp.route('/api/v1.0/project', methods=['GET'])
def index():
    response = Projeto.index()

    return response, Response(status=200)



@project_bp.route('/api/v1.0/project', methods=['POST'])
def create():
    """
    Recebe um json como data e cria um novo Projeto no banco
    """

    return project, Response(status=201)



@project_bp.route('/api/v1.0/project/<idProject>', methods=['GET'])
def show(idProject):
    request_json = request.get_json()

    idProject = request_json['data']['idProject']

    project = Projeto.show(idProject)

    return project, Response(status=200)



@project_bp.route('/api/v1.0/project/<idProject>', methods=['PUT'])
def upgrade(idProject):
    request_json = request.get_json()

    idProject = request_json['data']['idProject']
    # get another request body data here

    project = Projeto.upgrade(idProject)

    return project, Response(status=200)



@project_bp.route('/api/v1.0/project/<idProject>', methods=['DELETE'])
def destroy(idProject):
    request_json = request.get_json()

    idProject = request_json['data']['idProject']

    project = Projeto.destroy(idProject)

    return project, Response(status=200)


@project_bp.route('/api/v1.0/project/<idProject>/user_in_project', methods=['GET'])
def user_in_project(idProject):
    request_json = request.get_json()

    idProject = request_json['data']['idProject']

    project = Projeto.user_in_project(idProject)

    return project, Response(status=200)