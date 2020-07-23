import datetime
import json

from app.main.create_app import db
from app.main.model.main_models import TarefaTable


def create_task(data):
    now = datetime.datetime.today().strftime('%Y-%m-%d')
    """
        Criar nova task
        @param:  data = dict/json corpo da requisição enviado via post
    """

    task = TarefaTable.query.filter_by(nome=data['nome']).first()
    if not task:
        new_task = TarefaTable(
            Grupo_idGrupo=data['Grupo_idGrupo'],
            Frequencia_idFrequencia=data['Frequencia_idFrequencia'],
            Raridade_idRaridade=data['Raridade_idRaridade'],
            dataAbertura=now,
            nome=data['nome'],
            descricao=data['descricao'],
            prazo=now + datetime.timedelta(days=2),
            status=data['status']
        )
        __save_changes(new_task)
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


def index_task():
    return TarefaTable.query.all()


def update_task(idTarefa, data):
    task = TarefaTable.query.filter_by(idTarefa=idTarefa).first()
    if task:
        TarefaTable.update().where(idTarefa=idTarefa).values(data)
        response_object = {
            'status': 'success',
            'message': 'Successfully update'
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Fail update, check the values and taskId'
        }
        return response_object, 400


def delete_task(idTarefa):
    task = TarefaTable.query.filter_by(idTarefa=idTarefa).first()
    if task:
        __delete_instance(task=task)
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


def show_task(idTarefa):
    return TarefaTable.query.filter_by(idTarefa=idTarefa).first()


def get_status(idTarefa):
    status = db.session.query(TarefaTable.status).filter(
        TarefaTable.idTarefa == idTarefa).scalar()
    return status


def __save_changes(data):
    db.session.add(data)
    db.session.commit()


def __delete_instance(task):
    db.session.delete(task)
    db.session.commit()
