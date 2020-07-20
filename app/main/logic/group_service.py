import datetime

from app.main.create_app import db
from app.main.model.main_models import GrupoTable


def create_new_group(data):
    now = datetime.datetime.now()
    """
        Cria novo  grupo
        param: data = dict/json com as informacoes do grupo 
        passado via request
    """

    group = GrupoTable.query.filter_by(idGrupo=data['idGrupo']).first()
    if not group:
        new_group = GrupoTable(
            idGrupo=data['idGrupo'],
            Loja_idLoja=data['Loja_idLoja'],
            dataCriacaO=datetime.datetime.now(),
            dataEncerramento=now + datetime.timedelta(hours=24),
            nome=data['nome'],
            descricao=data['descricao']
        )
        __save_changes(new_group)
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


def index_group():
    return GrupoTable.query.all()


def update_group(idGrupo, data):
    group = GrupoTable.query.filter_by(idGrupo=idGrupo).first()
    if group:
        GrupoTable.update().where(idGrupo=idGrupo).values(data)
        response_object = {
            'status': 'success',
            'message': 'Successfully update'
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Fail update, check the values and userId'
        }
        return response_object, 400

def delete_group(idGrupo):
    group = GrupoTable.query.filter_by(idGrupo=idGrupo).first()
    if group:                       
        delete_instance(group=group)
        response_object = {
            'status': 'success',
            'message': 'Successfully deleted'
        }
        return response_object,  200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Fail delete'
        }
        return response_object, 400

def show_group(idGrupo):
    return GrupoTable.queryy.filter_by(idGrupo=idGrupo).first()


def __save_changes(data):
    db.session.add(data)
    db.session.commit()


def __delete_instance(group):
    db.session.delete(group)
    db.session.commit()
