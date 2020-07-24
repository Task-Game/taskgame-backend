from flask import request
from flask_restplus import Resource

from app.main.utils.dto_objects import ItemDto
from app.main.logic.item_service import *

api = ItemDto.api
_item = ItemDto.item


@api.route('/api/v1/item')
class ItemCreateIndex(Resource):
    @api.doc('Retorna todos os item do banco')
    @api.marshal_list_with(_item, envelope='data')
    def get(self):
        """
        Retorna todos os itens do banco(index)

        Args:
            self (class.self):

        """
        return index_item()

    @api.response(201, 'Item criado com  sucesso')
    @api.doc('Cria novo item utilizando as informacoes passadas via json')
    @api.expect(_item, validation=True)
    def post(self):
        """
        Cria  novo item(create)

        Args:
            self (class.self):

        """
        data = request.json
        return create_new_item(data)


@api.route('/api/v1/item/<item_id>')
@api.param('item_id', 'identificacao do item')
@api.response(404, 'Item not found')
class ItemWithParam(Resource):

    @api.doc('Atuliza o item')
    @api.expect(_item, validade=True)
    def patch(self, item_id):
        """
        Alterar  valores do item (update)

        Args:
            self (class.self):
            item_id (id do item que se quer alterar):

        """
        data = request.json
        item = show_item(idItem=item_id)

        if not item:
            api.abort(404)
            return "Item don't exist"
        else:
            return update_item(idItem=item_id, data=data)

    @api.doc('Mostra apenas um item')
    @api.marshal_with(_item)
    def get(self, item_id):
        """
        Retorna  somente  um item pelo id (show)

        Args:
            self (class.self):
            item_id (id do item que se quer alterar):
            
        """

        item = show_item(idItem=item_id)
        if not item:
            api.abort(404)
            return "Item don't exist"
        else:
            return item


    @api.doc('Delete item')
    def delete(self, item_id):
        """
        Delete item a partir do id (delete)

        Args:
            self (class.self):
            item_id (id do item que se quer alterar):

        """
        item = show_item(idItem=item_id)

        if not item:
            api.abort(404)
            return "Item don't exist"
        else:
            return delete_item(idItem=item_id)