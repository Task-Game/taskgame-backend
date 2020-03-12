from flask import Blueprint, make_response, request
from .Usuario import Usuario
import json
user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/api/v1/user/login', methods=['GET'])
def user_login():
    request_json = request.get_json()

    email = request_json['data']['email']
    senha = request_json['data']['senha']

    loggin_aprove = Usuario.authenticated_login(email, senha)

    return loggin_aprove
