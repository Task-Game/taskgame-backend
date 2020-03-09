from flask_sqlalchemy import SQLAlchemy
from app import create_app
from ..manager import db


class Usuario(db.Model):
    """
    Classe model responsavel pelos dados do usuario
    """

    __tablename__ = 'Usuario'
    idUsuario = db.Column(db.Integer,
                          primary_key=True)

    TipoUsuario_idTipoUsuario = db.relationship('TipoUsuario')

    nome = db.Column(db.String(80),
                     unique=False,
                     nullable=False,
                     index=False)

    email = db.Column(db.String(60),
                      unique=True,
                      nullable=False,
                      index=True)

    dataNascimento = db.Column(db.DateTime,
                               unique=False,
                               nullable=False,
                               index=False)

    senha = db.Column(db.String(18),
                      unique=False,
                      nullable=False,
                      index=False)

    pontos = db.Column(db.Integer,
                       unique=False,
                       nullable=True,
                       index=False)

    def __repr__(self):
        return '<Email {}>'.format(self.email)


class Frequencia(db.Model):
    __tablename__ = "Frequencia"

    idFrequencia = db.Column(db.Integer,
                             primary_key=True)

    descricao = db.Column(db.String(50))

    def __repr__(self):
        return '<descricao {}>'.format(self.descricao)


class Item(db.Model):
    __tablename__ = 'Item'

    idItem = db.Column(db.Integer,
                       primary_key=True)

    Loja_idLoja = db.relationship('Loja')

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

class Meta(db.Model):
    __tablename__ = 'Meta'

    idMeta = db.Column(db.Integer,
                       primary_key=True)
    
    Tarefa_idTarefa = db.relationship('Tarefa')

    descricao = db.Column(db.String(100),
                          unique=False,
                          nullable=False,
                          index=False)

    feito = db.Column(db.Boolean,
                      unique=False,
                      nullable=False,
                      index=True)