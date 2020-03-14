from flask import Blueprint, make_response, request
from .Usuario import Usuario
import json
user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/api/v1.0/user/', methods=['GET'])
def index():
    response = Usuario.index()

    return response


@user_bp.route('/api/v1.0/user/new', methods=['GET'])
def new():
    pass


@user_bp.route('/api/v1.0/user/', methods=['POST'])
def create():
    response = Usuario.create()

    return response

@user_bp.route('/api/v1.0/user/<:idUser>', methods=['GET'])
def show(idUser):
    request_json = request.get_json()

    idUser = request_json['data']['idUser']

    user = Usuario.show(idUser)

    return user


@user_bp.route('/api/v1.0/user/<:idUser>/edit', methods=['GET'])
def edit(idUSer):
    request_json = request.get_json()

    idUser = request_json['data']['idUser']
    # get another request body data here

    user = Usuario.edit(idUser)

    return user

@user_bp.route('/api/v1.0/user/<:idUser>', methods=['PUT'])
def upgrade(idUser):
    request_json = request.get_json()

    idUser = request_json['data']['idUser']
    # get another request body data here

    user = Usuario.upgrade(idUser)

    return user


@user_bp.route('/api/v1.0/user/<:idUser>', methods=['DELETE'])
def destroy(idUser):
    request_json = request.get_json()

    idUser = request_json['data']['idUser']

    user = Usuario.destroy(idUser)

    return user


@user_bp.route('/api/v1/user/login', methods=['GET'])
def user_login():
    request_json = request.get_json()

    email = request_json['data']['email']
    senha = request_json['data']['senha']

    loggin_aprove = Usuario.authenticated_login(email, senha)

    return loggin_aprove

