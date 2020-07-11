from flask import request
from flask_restplus import Resource

from ..utils.dto_objects import UserDto
from ..logic.user_service import *

api = UserDto.api
_user = UserDto.user


@api.route('/api/v1/users')
class UserCreateIndex(Resource):

    @api.route(methods=['GET'])
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
    def create(self):
        """
        Criar novo usuario (create)
        """
        data = request.json
        return create_new_user(data=data)


@api.route('/api/v1/users/<user_id>')
@api.param('idUser', 'Identificacão do usuario')
@api.response(404, 'User not found')
class UserWithParam(Resource):
    @api.doc("Atualizar usuario")
    def patch(self, idUsuario):
        """
        Atualiza o usuario passado por id
        """

        data = request.json
        user = show_user(idUsuario=idUsuario)

        if not user:
            api.abort(404)
        else:
            return update_user(idUsuario=idUsuario, data=data)

    @api.doc("Delete usuario")
    def delete(self, idUsuario):
        """
        Delete  o usuario passado via id
        """

        user = show_user(idUsuario=idUsuario)

        if not user:
            api.abort(404)
        else:
            return delete_user(idUsuario=idUsuario)

    @api.doc("Mostar usuario especifico")
    @api.marshal_with(_user)
    def get(self, idUsuario):
        """
        Buscar  usuario especifico de acordo com o id
        """

        user = show_user(idUsuario=Idusuario)
        if not user:
            api.abort(404)
        else:
            return user
