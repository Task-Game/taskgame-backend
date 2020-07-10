from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace(
        'user', description='Opeacoes envolvendo a entidade "Usuario" ')
    user = api.model('user', {
        'nome': fields.String(required=True, description='Nome do usuario'),
        'email': fields.String(required=True, description='Email do usuario'),
        'cargo': fields.String(required=True, description='Cargo do usuario'),
        'senha': fields.String(required=True, description='Senha do usuario'),
    })
