from flask_sqlalchemy import SQLAlchemy
from manager import db
import datetime


class Frequencia(db.Model):
    __tablename__ = "Frequencia"

    idFrequencia = db.Column(db.Integer,
                             primary_key=True)

    descricao = db.Column(db.String(50))

    tarefa = db.relationship('Tarefa', backref="frequencia")


class Meta(db.Model):
    __tablename__ = 'Meta'

    idMeta = db.Column(db.Integer,
                       primary_key=True)

    Tarefa_idTarefa = db.Column(db.Integer,
                                db.ForeignKey('Tarefa.idTarefa'))

    descricao = db.Column(db.String(100),
                          unique=False,
                          nullable=False,
                          index=False)

    feito = db.Column(db.Boolean,
                      unique=False,
                      nullable=False,
                      index=True)


class Raridade(db.Model):
    __tablename__ = 'Raridade'

    idRaridade = db.Column(db.Integer,
                           primary_key=True)

    descricao = db.Column(db.String(100),
                          unique=False,
                          nullable=False,
                          index=False)

    recompensa = db.Column(db.Integer,
                           unique=False,
                           nullable=False,
                           index=True)

    tarefa = db.relationship('Tarefa', backref="raridade")


class TipoUsuario(db.Model):
    __tablename__ = 'TipoUsuario'

    idTipoUsuario = db.Column(db.Integer,
                              primary_key=True)

    descricao = db.Column(db.String(100),
                          unique=False,
                          nullable=False,
                          index=False)

    usuario = db.relationship('Usuario', backref='tipoUsuario')


class Loja(db.Model):
    __tablename__ = 'Loja'

    idLoja = db.Column(db.Integer,
                       primary_key=True)

    Projeto_idProjeto = db.Column(db.Integer,
                                  db.ForeignKey('Projeto.idProjeto'))

    dataAbertura = db.Column(db.DateTime,
                             unique=False,
                             nullable=False,
                             index=False,
                             default=datetime.datetime.now())

    dataFechamento = db.Column(db.DateTime,
                               unique=False,
                               nullable=False,
                               index=False)

    item = db.relationship('Item', backref='item')


class Item(db.Model):
    __tablename__ = 'Item'

    idItem = db.Column(db.Integer,
                       primary_key=True)

    Loja_idLoja = db.Column(db.Integer,
                            db.ForeignKey('Loja.idLoja'))

    nome = db.Column(db.String(50),
                     unique=True,
                     nullable=False,
                     index=False)

    descricao = db.Column(db.String(100),
                          unique=False,
                          nullable=False,
                          index=False)

    valor = db.Column(db.Integer,
                      unique=False,
                      nullable=False,
                      index=False)


class Projeto(db.Model):
    __tablename__ = 'Projeto'

    idProjeto = db.Column(db.Integer,
                          primary_key=True)

    loja = db.relationship('Loja', backref="projeto")

    dataAbertura = db.Column(db.DateTime,
                             unique=False,
                             nullable=False,
                             index=False,
                             default=datetime.datetime.now())

    dataFechamento = db.Column(db.DateTime,
                               unique=False,
                               nullable=False,
                               index=False)

    titulo = db.Column(db.String(50),
                       unique=False,
                       nullable=False,
                       index=False)

    descricao = db.Column(db.String(100),
                          unique=False,
                          nullable=False,
                          index=False)

    prazo = db.Column(db.DateTime,
                      unique=False,
                      nullable=True,
                      index=False)


class Tarefa(db.Model):
    __tablename__ = 'Tarefa'

    idTarefa = db.Column(db.Integer,
                         primary_key=True)

    Projeto_idProjeto = db.Column(db.Integer,
                                  db.ForeignKey('Projeto.idProjeto'),
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
                             index=False,
                             default=datetime.datetime.now())

    nome = db.Column(db.String(100),
                     unique=True,
                     nullable=False,
                     index=False)

    descricao = db.Column(db.String(100),
                          unique=False,
                          nullable=False,
                          index=False)

    prazo = db.Column(db.DateTime,
                      unique=False,
                      nullable=False,
                      index=False)

    recompensa = db.Column(db.Integer,
                           unique=True,
                           nullable=False,
                           index=False)

    status = db.Column(db.Integer,
                       unique=False,
                       nullable=True,
                       index=False)


class Usuario(db.Model):
    """
    Classe model responsavel pelos dados do usuario
    """

    __tablename__ = 'Usuario'
    idUsuario = db.Column(db.Integer,
                          primary_key=True)

    TipoUsuario_idTipoUsuario = db.Column(db.Integer,
                                          db.ForeignKey(
                                              'TipoUsuario.idTipoUsuario'),
                                          default=0)

    nome = db.Column(db.String(80),
                     unique=False,
                     nullable=False,
                     index=False)

    email = db.Column(db.String(60),
                      unique=True,
                      nullable=False,
                      index=True)

    dataCriacao = db.Column(db.DateTime,
                            unique=False,
                            nullable=False,
                            index=False,
                            default=datetime.datetime.now())

    dataNascimento = db.Column(db.DateTime,
                               unique=False,
                               nullable=False,
                               index=False)

    senha = db.Column(db.String(250),
                      unique=False,
                      nullable=False,
                      index=False)

    pontos = db.Column(db.Integer,
                       unique=False,
                       nullable=True,
                       index=False,
                       default=0)

    usuario_projeto = db.relationship(
        'usuario_projeto', backref="usuario_projeto")

    usuario_projeto = db.relationship(
        'usuario_tarefa', backref="usuario_tarefa")


usuario_projeto = db.Table('usuario_projeto',
                           db.Column('idUsuarioProjeto', db.Integer,
                                     primary_key=True),
                           db.Column('Usuario_idUsuario', db.Integer,
                                     db.ForeignKey('Usuario.idUsuario')),

                           db.Column('Projeto_idTarefa', db.Integer,
                                     db.ForeignKey('Projeto.idProjeto')))

usuario_tarefa = db.Table('usuario_tarefa',
                          db.Column('idUsuarioTarefa', db.Integer,
                                    primary_key=True),
                          db.Column('Usuario_idUsuario', db.Integer,
                                    db.ForeignKey('Usuario.idUsuario')),
                          db.Column('Tarefa_idTarefa', db.Integer,
                                    db.ForeignKey('Tarefa.idTarefa')))