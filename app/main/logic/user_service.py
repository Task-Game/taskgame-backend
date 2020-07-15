import uuid
import datetime

from app.main.create_app import db 
from app.main.model.user import UserTable


def create_new_user(data):
    """
        Cria novo  usuario
        param: data = dict/json com as informacoes do usuario 
        passado via request
    """

    user = UserTable.query.filter_by(email=data['email']).first()
    if not user:
        new_user = UserTable(
            nome=data['nome'],
            email=data['email'],
            cargo=data['cargo'],
            dataCriacao=datetime.datetime.now(),
            codigoConfirmacao='000111222', # NOTE: alterar p/ codigo gerado aleatoriamente
            senha=data['senha'],
            credito=0
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Already registered, please login'
        }
        return response_object, 409

def index_user():
    response_data = UserTable.query.all()
    if response_data:
        response_object = {
            'status': 'success',
            'message': 'Successfully index'
        }
        return response_data, response_object,  200
    else:
        response_object = {
            'status':'fail',
            'message':'Fail indexing data'
        }
        return response_object, 400

def update_user(idUsuario, data):
    user = UserTable.query.filter_by(idUsuario=idUsuario).first()
    if user:
        for key, value in data:
            if key is not 'idUsuario':
                user.key = value    
                db.session.commit() 
        response_object = {
            'status': 'success',
            'message': 'Successfully update'
        }
        return response_object, 200
    else:
        response_object = {
            'status':'fail',
            'message':'Fail update, check the values and userId'
        }
        return response_object, 400

def delete_user(idUsuario):
    user = UserTable.query.filter_by(idUsuario=idUsuario).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully deleted'
        }
        return response_object,  200
    else:
        response_object = {
            'status':'fail',
            'message':'Fail delete'
        }
        return response_object, 400


def show_user(idUsuario):
    response_data = UserTable.query.filter_by(idUsuario=idUsuario).first()

    if response_data:
        response_object = {
            'status': 'success',
            'message': 'Successfully showing'
        }
        return response_data, response_object,  200
    else:
        response_object = {
            'status':'fail',
            'message':'Fail show data'
        }
        return response_object, 400

def save_changes(data):
    db.session.add(data)
    db.session.commit()
