from ..create_app import db, flask_bcrypt
from datetime import datetime
import hashlib

usuario_tarefa = db.Table('usuario_tarefa',
                          db.Column('idUsuarioTarefa', db.Integer,
                                    primary_key=True),

                          db.Column('Usuario_idUsuario', db.Integer,
                                    db.ForeignKey('Usuario.idUsuario')),

                          db.Column('Tarefa_idTarefa', db.Integer,
                                    db.ForeignKey('Tarefa.idTarefa'))
                          )

usuario_grupo = db.Table('usuario_grupo',
                         db.Column('idUsuarioGrupo', db.Integer,
                                   primary_key=True),

                         db.Column('Usuario_idUsuario', db.Integer,
                                   db.ForeignKey('Usuario.idUsuario')),

                         db.Column('Grupo_idGrupo', db.Integer,
                                   db.ForeignKey('Grupo.idGrupo'))

                         )


class GrupoTable(db.Model):
    __tablename__ = 'Grupo'

    idGrupo = db.Column(db.Integer,
                        primary_key=True)

    Loja_idLoja = db.Column(db.Integer,
                            db.ForeignKey('Loja.idLoja'))

    dataCriacao = db.Column(db.DateTime,
                            unique=False,
                            nullable=False,
                            default=datetime.now())

    dataEncerramento = db.Column(db.DateTime,
                                 unique=False,
                                 nullable=False)

    nome = db.Column(db.String(50),
                     unique=False,
                     nullable=False)

    descricao = db.Column(db.String(100),
                          unique=False,
                          nullable=False)

    grupoUser = db.relationship('UserTable', secondary=usuario_grupo)


class TarefaTable(db.Model):
    __tablename__ = 'Tarefa'

    idTarefa = db.Column(db.Integer,
                         primary_key=True)

    Grupo_idGrupo = db.Column(db.Integer,
                              db.ForeignKey('Grupo.idGrupo'),
                              nullable=True)

    Raridade_idRaridade = db.Column(db.Integer,
                                    db.ForeignKey('Raridade.idRaridade'))

    Frequencia_idFrequencia = db.Column(db.Integer,
                                        db.ForeignKey(
                                            'Frequencia.idFrequencia'))

    dataAbertura = db.Column(db.DateTime,
                             unique=False,
                             nullable=False,
                             default=datetime.now())

    nome = db.Column(db.String(100),
                     nullable=False)

    descricao = db.Column(db.String(100),
                          unique=False,
                          nullable=False)

    prazo = db.Column(db.DateTime,
                      unique=False,
                      nullable=False)

    status = db.Column(db.Boolean,
                       unique=False,
                       nullable=True)

    tarefaUser = db.relationship('UserTable', secondary=usuario_tarefa)


class UserTable(db.Model):
    """
    Classe model responsavel pelos dados do usuario
    """

    __tablename__ = 'Usuario'

    idUsuario = db.Column(db.Integer,
                          primary_key=True)

    nome = db.Column(db.String(80), unique=False, nullable=False)

    email = db.Column(db.String(60), unique=True, nullable=False)

    cargo = db.Column(db.String(50), unique=False, nullable=True)

    dataCriacao = db.Column(db.DateTime, unique=False, nullable=False,
                            default=datetime.now())

    codigoConfirmacao = db.Column(db.String(50), unique=False, nullable=False)

    senha = db.Column(db.String(80), unique=False, nullable=True)

    credito = db.Column(db.Integer, unique=False, nullable=True,)

    userTarefa = db.relationship('TarefaTable', secondary=usuario_tarefa)

    userGrupo = db.relationship('GrupoTable', secondary=usuario_grupo)
