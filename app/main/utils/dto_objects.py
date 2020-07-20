from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace(
        'user', description='Operacoes relacionadas com o "Usuário"')
    user = api.model('user', {
        'idUsuario': fields.Integer(required=False, description='Id do usuario'),
        # TODO: Verificar se existe no corpo da requisicão
        'nome': fields.String(required=False, description='Nome do usuario'),
        # TODO: Verificar se existe no corpo da requisicão
        'email': fields.String(required=False, description='Email do usuario'),
        'dataCriacao': fields.DateTime(required=False, description='Data de criacao do usuario'),
        'cargo': fields.String(required=False, description='Cargo do usuario'),
        'credito': fields.Integer(required=False, description='créditos do usuario'),
        # TODO: Verificar se existe no corpo da requisicão
        'senha': fields.String(required=False, description='Senha do usuario'),
    })


class TaskDto:
    api = Namespace(
        'task', description='Operacoes relacionadas com a "Tarefa"'
    )
    # TODO: Fazer a verificacao dos parametros: idTarefa, Nome, Data Abertura, Descicao, Status
    task = api.model('task', {
        'idTarefa': fields.Integer(required=False, description='Id referente a tarefa'),
        'Frequencia_idFrequencia': fields.Integer(required=False, description='Id da frequencia relacionada a tarefa'),
        'Raridade_idRaridade': fields.Integer(required=False, description='Id da raridade referente a tarefa'),
        'dataAbertura': fields.DateTime(required=False, description='Data de abertura ta tarefa'),
        'nome': fields.String(required=False, description='Titulo da tarefa'),
        'descricao': fields.String(required=False, description='Descricao da tarefa'),
        'prazo': fields.DateTime(required=False, description='Prazo da tarefa'),
        'status': fields.Boolean(required=False, description='Status da tarefa'),
    })

class GroupDto:
    api = Namespace(
        'group', description='Operacoes relacionadas com o "Grupo"'
    )

    group = api.model('group',{
        'idGrupo': fields.Integer(required=False, description='Id referente ao grupo'),
        'Loja_idLoja': fields.Integer(required=False, description='Id referente a loja'),
        'dataCriacao': fields.DateTime(required=False, description='Data da criacão do grupo'),
        'dataEncerramento': fields.DateTime(required=False, description='Data de encerramento do grupo'),
        'nome': fields.String(required=False, descriptio='Nome do grupo'),
        'descricao': fields.String(required=False, description='Descricao do grupo')
    })