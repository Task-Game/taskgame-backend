import datetime

from app.main.create_app import db
from app.main.model.item import ItemTable
from app.main.model.store import LojaTable


def create_new_item(data):
    """
    Cria novo item com dados passados via request
    """

    new_item = ItemTable(
        Loja_idLoja=data['Loja_idLoja'],
        nome=data['nome'],
        descricao=data['descricao'],
        valor=data['valor']
    )

    __save_changes(new_item)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered'
    }

    return response_object, 201

def index_item():
    return ItemTable.query.all()

def update_item(idItem, data):
    item = ItemTable.query.filter_by(idItem=idItem).first()
    if item:
        ItemTable.query.filter(ItemTable.idItem == idItem).update(data)
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

def delete_item(idItem):
    item = ItemTable.query.filter_by(idItem=idItem).first()
    if item:
        __delete_instance(item=item)
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

def show_item(idItem):
    return ItemTable.query.filter_by(idItem=idItem).first()


def __save_changes(data):
    db.session.add(data)
    db.session.flush()
    db.session.commit()


def __delete_instance(item):
    db.session.delete(item)
    db.session.commit()
