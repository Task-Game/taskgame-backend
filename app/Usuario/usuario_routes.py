from flask import Blueprint, request, Response
from .Usuario import Usuario
import json
user_bp = Blueprint('user_bp', __name__)


# @user_bp.route('/api/v1.0/users', methods=['GET'])
# def index():
#     response = Usuario.index()

#     return response, Response(status=200)


@user_bp.route('/api/v1.0/users', methods=['POST'])
def create():
    """
    Recebe um json como data e cria um novo usuario no banco
    """

    if request.is_json:
        request_json = request.get_json()

        email = request_json['data']['email']
        nome = request_json['data']['nome']
        senha = request_json['data']['senha']

        user_create = Usuario.create(email, nome, senha)

        if userCreate:
            return Response(status=201)
        else:
            return user_create, Response(status=400)

    

# @user_bp.route('/api/v1.0/users/<idUser>', methods=['GET'])
# def show(idUser):
#     request_json = request.get_json()

#     idUser = request_json['data']['idUser']

#     user = Usuario.show(idUser)

#     return user, Response(status=200)


# @user_bp.route('/api/v1.0/users/<idUser>', methods=['PUT'])
# def upgrade(idUser):
#     request_json = request.get_json()

#     idUser = request_json['data']['idUser']
#     # get another request body data here

#     user = Usuario.upgrade(idUser)

#     return user, Response(status=200)


# @user_bp.route('/api/v1.0/users/<idUser>', methods=['DELETE'])
# def destroy(idUser):
#     request_json = request.get_json()

#     idUser = request_json['data']['idUser']

#     user = Usuario.destroy(idUser)

#     return user, Response(status=200)


# @user_bp.route('/api/v1/user/login', methods=['GET'])
# def login():
#     request_json = request.get_json()

#     email = request_json['data']['email']
#     senha = request_json['data']['senha']

#     loggin_aprove = Usuario.authenticated_login(email, senha)

#     return loggin_aprove, Response(status=200)


# @user_bp.route('/api/v1.0/users/<idUser>/tasks_in_user', methods=['GET'])
# def tasks_in_user(idUser):
#     request_json = request.get_json()

#     idUser = request_json['data']['idUser']

#     user = Usuario.tasks_in_user(idUser)

#     return user, Response(status=200)

