from flask import Blueprint, request, Response
from .Meta import Meta
import json
goal_bp = Blueprint('goal_bp', __name__)


@goal_bp.route('/api/v1.0/goal', methods=['GET'])
def index():
    response = Meta.index()

    return response, Response(status=200)



@goal_bp.route('/api/v1.0/goal', methods=['POST'])
def create():
    """
    Recebe um json como data e cria um novo Meta no banco
    """

    return goal, Response(status=201)



@goal_bp.route('/api/v1.0/goal/<idGoal>', methods=['GET'])
def show(idGoal):
    request_json = request.get_json()

    idGoal = request_json['data']['idGoal']

    goal = Meta.show(idGoal)

    return goal, Response(status=200)



@goal_bp.route('/api/v1.0/goal/<idGoal>', methods=['PUT'])
def upgrade(idGoal):
    request_json = request.get_json()

    idGoal = request_json['data']['idGoal']
    # get another request body data here

    goal = Meta.upgrade(idGoal)

    return goal, Response(status=200)



@goal_bp.route('/api/v1.0/goal/<idGoal>', methods=['DELETE'])
def destroy(idGoal):
    request_json = request.get_json()

    idGoal = request_json['data']['idGoal']

    goal = Meta.destroy(idGoal)

    return goal, Response(status=200)


@goal_bp.route('api/v1.0/goal/<idGoal>/goal_in_task', methods=['GET'])
def goal_in_task(idGoal):
    request_json = request.get_json()

    idGoal = request_json['data']['idGoal']

    goal = Metas.goal_in_task(idGoal)

    return goal, Response(status=200)