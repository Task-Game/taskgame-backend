import datetime

from app.main.create_app import db
from app.main.model.main_models import usuario_tarefa

def log_userTask(idUsuario, idTarefa):
    newLog = usuario_tarefa(
        Usuario_idUsuario=idUsuario,
        Tarefa_idTarefa=idTarefa
    )
    __save_changes(newLog)


def __save_changes(data):
    db.session.add(data)
    db.session.commit()
