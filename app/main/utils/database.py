from flask_sqlalchemy import SQLAlchemy
from manager import db
import datetime
import hashlib


class FrequenciaTable(db.Model):
    __tablename__ = "Frequencia"

    idFrequencia = db.Column(db.Integer,
                             primary_key=True)

    descricao = db.Column(db.String(50),
                          nullable=False)

    # A chave desta tabela esta na que se refere
    tarefa = db.relationship('Tarefa', backref="frequencia")


class ChecklistTable(db.Model):
    __tablename__ = 'Checklist'

    idChecklist = db.Column(db.Integer,
                            primary_key=True)

    Tarefa_idTarefa = db.Column(db.Integer,
                                # A chave de tarefa esta aqui
                                db.ForeignKey('Tarefa.idTarefa'),
                                nullable=False)

    descricao = db.Column(db.String(100),
                          unique=False,
                          nullable=False)

    feito = db.Column(db.Boolean,
                      unique=False,
                      nullable=False)


class RaridadeTable(db.Model):
    __tablename__ = 'Raridade'

    idRaridade = db.Column(db.Integer,
                           primary_key=True)

    descricao = db.Column(db.String(100),
                          unique=False,
                          nullable=False)

    recompensa = db.Column(db.Integer,
                           unique=False,
                           nullable=False,
                           index=True)

    # O id raridade esta na tabela tarefa
    tarefa = db.relationship('Tarefa', backref="raridade")
    # O id raridade esta na tabela item
    item = db.relationship('Item', backref="raridade")


class LojaTable(db.Model):
    __tablename__ = 'Loja'

    idLoja = db.Column(db.Integer,
                       primary_key=True)

    dataAbertura = db.Column(db.DateTime,
                             unique=False,
                             nullable=False,
                             default=datetime.datetime.now())

    dataFechamento = db.Column(db.DateTime,
                               unique=False,
                               nullable=False)

    item = db.relationship('Item', backref='loja')
    grupo = db.relationship('Grupo', backref='loja')


class ItemTable(db.Model):
    __tablename__ = 'Item'

    idItem = db.Column(db.Integer,
                       primary_key=True)

    Loja_idLoja = db.Column(db.Integer,
                            db.ForeignKey('Loja.idLoja'))

    Raridade_idRaridade = db.Column(db.Integer,
                                    db.ForeignKey('Raridade.idRaridade'))

    nome = db.Column(db.String(50),
                     unique=True,
                     nullable=False)

    descricao = db.Column(db.String(100),
                          unique=False,
                          nullable=False)

    valor = db.Column(db.Integer,
                      unique=False,
                      nullable=False)


class GrupoTable(db.Model):
    __tablename__ = 'Grupo'

    idGrupo = db.Column(db.Integer,
                        primary_key=True)

    Loja_idLoja = db.Column(db.Integer,
                            db.ForeignKey('Loja.idLoja'))

    dataCriacao = db.Column(db.DateTime,
                            unique=False,
                            nullable=False,
                            default=datetime.datetime.now())

    dataEncerramento = db.Column(db.DateTime,
                                 unique=False,
                                 nullable=False)

    nome = db.Column(db.String(50),
                     unique=False,
                     nullable=False)

    descricao = db.Column(db.String(100),
                          unique=False,
                          nullable=False)

    usuario_grupo = db.relationship(
        'usuario_grupo', backref="usuario")


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
                                            'Frequencia.idFrequencia'),
                                        nullable=True)

    dataAbertura = db.Column(db.DateTime,
                             unique=False,
                             nullable=False,
                             default=datetime.datetime.now())

    nome = db.Column(db.String(100),
                     unique=True,
                     nullable=False)

    descricao = db.Column(db.String(100),
                          unique=False,
                          nullable=False)

    prazo = db.Column(db.DateTime,
                      unique=False,
                      nullable=False)

    recompensa = db.Column(db.Integer,
                           unique=True,
                           nullable=False)

    status = db.Column(db.Boolean,
                       unique=False,
                       nullable=True)

    usuario_tarefa = db.relationship(
        'usuario_tarefa', backref="tarefa")


class UsuarioTable(db.Model):
    """
    Classe model responsavel pelos dados do usuario
    """

    __tablename__ = 'Usuario'

    idUsuario = db.Column(db.Integer,
                          primary_key=True)

    nome = db.Column(db.String(80),
                     unique=False,
                     nullable=False)

    email = db.Column(db.String(60),
                      unique=True,
                      nullable=False)

    cargo = db.Column(db.String(50),
                        unique=False,
                        nullable=True)

    dataCriacao = db.Column(db.DateTime,
                            unique=False,
                            nullable=False,
                            default=datetime.datetime.now())

    codigoConfirmacao = db.Column(db.String(50),
                                  unique=False,
                                  nullable=False)

    senha = db.Column(db.String(250),
                      unique=False,
                      nullable=False)

    credito = db.Column(db.Integer,
                        unique=False,
                        nullable=True,)

    usuario_grupo = db.relationship(
        'usuario_grupo', backref="usuario")

    usuario_tarefa = db.relationship(
        'usuario_tarefa', backref="usuario")


usuario_grupo = db.Table('usuario_grupo',
                         db.Column('idUsuarioGrupo', db.Integer,
                                   primary_key=True),
                         db.Column('Usuario_idUsuario', db.Integer,
                                   db.ForeignKey('Usuario.idUsuario')),

                         db.Column('Grupo_idGrupo', db.Integer,
                                   db.ForeignKey('Grupo.idGrupo'))

                         )

usuario_tarefa = db.Table('usuario_tarefa',
                          db.Column('idUsuarioTarefa', db.Integer,
                                    primary_key=True),
                          db.Column('Usuario_idUsuario', db.Integer,
                                    db.ForeignKey('Usuario.idUsuario')),
                          db.Column('Tarefa_idTarefa', db.Integer,
                                    db.ForeignKey('Tarefa.idTarefa')))
