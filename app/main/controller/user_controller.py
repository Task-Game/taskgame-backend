from flask import request
from flask_restplus import Resource

from ..utils.dto_objects import UserDto
from ..logic.user_service import *

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserCreateIndex(Resource):

    @api.doc("Listar todos os usuarios")
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """
        Listar todos os usuarios (index/read)
        """
        return index_user()

    @api.response(201, "Usuario criado com sucesso.")
    @api.doc('Criar novo usuario')
    @api.expect(_user, validate=True)
    def post(self):
        """
        Criar novo usuario (create)
        """
        data = request.json
        return create_new_user(data=data)


@api.route('/<user_id>')
@api.param('user_id', 'Identificacão do usuario')
@api.response(404, 'User not found')
class UserWithParam(Resource):

    @api.doc("Atualizar usuario")
    @api.expect(_user, validate=True)
    def patch(self, user_id):
        """
        Atualiza o usuario passado por id (update)
        """

        data = request.json
        user = show_user(idUsuario=user_id)

        if not user:
            api.abort(404)
        else:
            return update_user(idUsuario=user_id, data=data)

    @api.doc("Delete usuario")
    def delete(self, user_id):
        """
        Delete o usuario passado via id(delete)
        """

        user = show_user(idUsuario=user_id)

        if not user:
            api.abort(404)
        else:
            return delete_user(idUsuario=user_id)

    @api.doc("Mostar usuario especifico")
    @api.marshal_with(_user)
    def get(self, user_id):
        """
        Buscar  usuario especifico de acordo com o id
        """

        user = show_user(idUsuario=user_id)
        if not user:
            api.abort(404)
        else:
            return user
