from flask import Blueprint, request, Response
from .Item import Item
import json
item_bp = Blueprint('item_bp', __name__)


@item_bp.route('/api/v1.0/item', methods=['GET'])
def index():
    response = Item.index()

    return response, Response(status=200)



@item_bp.route('/api/v1.0/item', methods=['POST'])
def create():
    """
    Recebe um json como data e cria um novo Item no banco
    """

    return item, Response(status=201)



@item_bp.route('/api/v1.0/item/<idItem>', methods=['GET'])
def show(idItem):
    request_json = request.get_json()

    idItem = request_json['data']['idItem']

    item = Item.show(idItem)

    return item, Response(status=200)



@item_bp.route('/api/v1.0/item/<idItem>', methods=['PUT'])
def upgrade(idItem):
    request_json = request.get_json()

    idItem = request_json['data']['idItem']
    # get another request body data here

    item = Item.upgrade(idItem)

    return item, Response(status=200)



@item_bp.route('/api/v1.0/item/<idItem>', methods=['DELETE'])
def destroy(idItem):
    request_json = request.get_json()

    idItem = request_json['data']['idItem']

    item = Item.destroy(idItem)

    return item, Response(status=200)


@item_bp.route('/api/v1.0/item/<idItem>/item_in_shop', methods=['GET'])
def item_in_shop(idItem):
    request_json = request.get_json()

    idItem = request_json['data']['idItem']

    item = Item.item_in_shop(idItem)

    return item, Response(status=200)