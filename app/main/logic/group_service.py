import datetime

from .user_service import show_user
from app.main.create_app import db
from app.main.model.main_models import GrupoTable, usuario_grupo
from app.main.model.store import LojaTable

NOW = datetime.datetime.today().strftime('%Y-%m-%d')


def __create_store(dataFechamento):
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
    user = show_user(data['idUsuario'])
    idLoja = __create_store(data['dataEncerramento'])

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

    new_group.membros.append(user)
    db.session.commit()

    return response_object, 201


def index_group():
    return GrupoTable.query.all()


def update_group(idGrupo, data):
    group = GrupoTable.query.filter_by(idGrupo=idGrupo).first()
    if group:
        GrupoTable.query.filter(GrupoTable.idGrupo == idGrupo).update(data)
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


def index_members(idGrupo):
    data = dict(db.session.query(usuario_grupo).filter_by(Grupo_idGrupo=idGrupo).all())

    return data


def __save_changes(data):
    db.session.add(data)
    db.session.flush()
    db.session.commit()


def __delete_instance(group):
    db.session.delete(group)
    db.session.commit()
