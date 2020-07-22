import datetime

from app.main.create_app import db
from app.main.model.main_models import usuario_grupo


def log_userGroup(idUsuario, idGrupo):
    new_log = usuario_grupo(
        Usuario_idUsuario=idUsuario,
        Grupo_idGrupo=idGrupo
    )
    __save_changes(newLog)


def __save_changes(data):
    db.session.add(data)
    db.session.commit()
