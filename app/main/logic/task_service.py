import datetime
import json

from app.main.create_app import db
from app.main.model.main_models import TarefaTable


def create_task(data):
    """
        Criar nova task
        @param:  data = dict/json corpo da requisição enviado via post
    """

    task = TarefaTable.query.filter_by(idTarefa=data['idTarefa']).first()
    if not task:
        new_task = TarefaTable(
            Frequencia_idFrequencia=data['idFrequencia'],
            Raridade_idRaridade=data['idRaridade'],
            dataAbertura=datetime.datetime.now(),
            nome=data['nome'],
            descricao=data['descricao'],
            prazo=data['prazo'],
            recompensa=data['recompensa'],
            status=data['status']
        )
        save_changes(new_task)
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
            'message': 'Fail update, check the values and userId'
        }
        return response_object, 400


def delete_task(idTarefa):
    task = TarefaTable.query.filter_by(idTarefa=idTarefa).first()
    if task:
        delete_intance(task=task)
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
    return TarefaTable.query(TarefaTable.status).filter_by(idTarefa=idTarefa).first()


def __save_changes(data):
    db.session.add(data)
    db.session.commit()


def __delete_intance(task):
    db.session.delete(task)
    db.session.commit()
