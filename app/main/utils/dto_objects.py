from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace(
        'user', description='Operacoes relacionadas com o "Usuario"')
    user = api.model('user', {
        'idUsuario': fields.Integer(required=False, description='Id do usuario'), 
        'nome': fields.String(required=False, description='Nome do usuario'),# NOTE: Verificar se existe no corpo da requisicão
        'email': fields.String(required=False, description='Email do usuario'), # NOTE: Verificar se existe no corpo da requisicão
        'dataCriacao':fields.DateTime(required=False, description='Data de criacao do usuario'),
        'cargo': fields.String(required=False, description='Cargo do usuario'),
        'credito': fields.Integer(required=False, description='creditos do usuario'),
        'senha': fields.String(required=False, description='Senha do usuario'), # NOTE: Verificar se existe no corpo da requisicão
    })
