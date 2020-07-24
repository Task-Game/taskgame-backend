from flask import request
from flask_restplus import Resource

from app.main.utils.dto_objects import GroupDto
from app.main.logic.group_service import *

api = GroupDto.api
_group = GroupDto.group


@api.route('/api/v1/group')
class GroupCreateIndex(Resource):
    @api.doc('Retorna todos os grupos')
    @api.marshal_list_with(_group, envelope='data')
    def get(self):
        """
        Retorna todas os grupos do banco (index)
        """
        return index_group()

    @api.response(201, 'Grupo criado com sucesso')
    @api.doc('Cria Grupo utilizando dados do corpo json enviado na request')
    @api.expect(_group, validation=True)
    def post(self):
        """
        Cria novo grupo (create)
        """

        data = request.json
        return create_new_group(data)


@api.route('/api/v1/group/<group_id>')
@api.param('group_id', 'Identificacão da tarefa')
@api.response(404, 'Group not found')
class GrupoWithParam(Resource):

    @api.doc('Atualizando grupo')
    @api.expect(_group, validade=True)
    def patch(self, group_id):
        """
        Atulizando infomacoes do grupo (update)
        """

        data = request.json
        group = show_group(idGrupo=group_id)

        if not group:
            api.abort(404)
            return "Group don't exists"
        else:
            return update_group(idGrupo=group_id, data=data)

    @api.doc('Mostrar apenas um grupo')
    @api.marshal_with(_group)
    def get(self, group_id):
        """
        Buscar grupo especifico (show)
        """

        group = show_group(idGrupo=group_id)
        if not group:
            api.abort(404)
        else:
            return group

    @api.doc('Deleta Grupo')
    def delete(self, group_id):
        """
        Deleta grupo passado via ID (delete)
        """

        group = show_group(idGrupo=group_id)

        if not group:
            api.abort(404)
            return "Group don't exists"
        else:
            return delete_group(idGrupo=group_id)


@api.route('/user/<group_id>')
@api.param('group_id', 'Identificacão do usuario')
@api.response(404, 'User not found')
class GroupUser(Resource):

    @api.doc('Retorna ids dos grupos em que o usuario esta')
    def get(self, group_id):
        """
        Retorna id dos usuario desse grupo

        Args:
            self (class.self):
            group_id (id do grupo):

        """
        group = show_group(idGrupo=group_id)
        

        if not group:
            api.abort(404)
            return "Group don't exists"
        else:
            return index_members(idGrupo=group_id)
