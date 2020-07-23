import datetime

from app.main.create_app import db
from app.main.model.main_models import GrupoTable, usuario_grupo
from app.main.model.store import LojaTable
import json

NOW = datetime.datetime.today().strftime('%Y-%m-%d')


def create_store(dataFechamento):
    new_store = LojaTable(
        dataFechamento=dataFechamento
    )
    __save_changes(new_store)
    return new_store.idLoja


def create_new_group(data):
    """
        Cria novo  grupo
        param: data = dict/json com as informacoes do grupo 
        passado via request
    """

    idLoja = create_store(data['dataEncerramento'])

    new_group = GrupoTable(
        Loja_idLoja=idLoja,
        dataCriacao=NOW,
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
        group.query.update(values=data)
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


# def __log_userGroup(idUsuario):
#    now = datetime.datetime.today().strftime('%Y-%m-%d')
#
#    group = last_group(now=now)
#    print(group)
#
#    new_log = usuario_grupo(
#        Usuario_idUsuario=idUsuario,
#        Grupo_idGrupo=idGrupo
#    )
#    __save_changes(newLog)


def __save_changes(data):
    db.session.add(data)
    db.session.flush()
    db.session.commit()


def __delete_instance(group):
    db.session.delete(group)
    db.session.commit()
