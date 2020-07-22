from flask import request
from flask_restplus import Resource

from ..utils.dto_objects import TaskDto
from ..logic.task_service import *

api = TaskDto.api
_task = TaskDto.task


@api.route('/')
class TaskCreateIndex(Resource):
    @api.doc('Retorna todas as tarefas')
    @api.marshal_list_with(_task, envelope='data')
    def get(self):
        """
        Retorna todas as tarefas registradas no banco (index/read)
        """
        return index_task()

    @api.response(201, 'Tarefa criada com sucesso')
    @api.doc('Cria tarefas via')
    @api.expect(_task, validation=True)
    def post(self):
        """
        Cria nova tarefa (create)
        """
        data = request.json
        return create_task(data=data)


@api.route('/<task_id>')
@api.param('task_id', 'Identificacão da tarefa')
@api.response(404, 'Task not found')
class TaskWithParam(Resource):

    @api.doc('Atualiza tarefa')
    @api.expect(_task, validade=True)
    def patch(self, task_id):
        """
        Atualiza dados da tarefa (update)
        """
        data = request.json
        task = show_task(idTarefa=task_id)

        if not task:
            api.abort(404)
            return "Task don't exists"
        else:
            return update_task(idTarefa=task_id, data=data)

    @api.doc('Deletar tarefa')
    def delete(self, task_id):
        """
        Deletar tarefa via idTarefa (delete)
        """
        task = show_task(idTarefa=task_id)

        if not task:
            api.abort(404)
            return "Task don't exists"
        else:
            return delete_task(idTarefa=task_id)

    @api.doc('Mostrar apenas uma tarefa')
    @api.marshal_with(_task)
    def get(self, task_id):
        """
        Buscar tarefa especifico (show)
        """

        task = show_task(idTarefa=task_id)
        if not task:
            api.abort(404)
        else:
            return task


@api.route('/api/v1/task/status/<task_id>')
@api.param('task_id', 'Identificacão da tarefa')
@api.response(404, 'Task not found')
class TaskUtils(Resource):

    @api.doc('Verificar status de uma tarefa')
    def get(self, task_id):
        """
        Retorna status da tarefa
        """

        task = get_status(idTarefa=task_id)
        if not task:
            api.abort(404)
        else:
            return task