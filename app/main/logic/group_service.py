import datetime

from app.main.create_app import db
from app.main.model.main_models import GrupoTable

def create_new_group(data):
    now = datetime.datetime.today().strftime('%Y-%m-%d')
    """
        Cria novo  grupo
        param: data = dict/json com as informacoes do grupo 
        passado via request
    """

    new_group = GrupoTable(
        Loja_idLoja=data['Loja_idLoja'],
        dataCriacao=now,
        dataEncerramento=data['dataEncerramento'],
        nome=data['nome'],
        descricao=data['descricao']
    )
    __save_changes(new_group)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered'
    }
    return response_object, 201


def index_group():
    return GrupoTable.query.all()


def update_group(idGrupo, data):
    group = GrupoTable.query.filter_by(idGrupo=idGrupo).first()
    if group:
        for key, values in data.items():
            group.key = values
            db.session.merge(group)
            db.session.commit()
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
        __delete_instance(group=group)
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
    return GrupoTable.query.filter_by(idGrupo=idGrupo).first()


def __save_changes(data):
    db.session.add(data)
    db.session.commit()


def __delete_instance(group):
    db.session.delete(group)
    db.session.commit()

