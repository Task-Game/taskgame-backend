from flask import Blueprint, make_response, request
from flask import corrent_app as app
from .Usuario import Usuario
user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/api/v1/user/', methods=['GET', 'PUT', 'POST', 'DELETE'])
def user_login():
    if request.method == 'GET':
        request_json = request.get_json()
        
        if request_json['action'] == 'login':
            email = request_json['data']['email']
            senha = request_json['data']['senha']
            
            loggin_aprove = Usuario.authenticated_login(email, senha)

    return loggin_aprove # True or False

    if request.method == 'POST':
        request_json = request.get_json()

        if request_json['action'] == 'register':
            

