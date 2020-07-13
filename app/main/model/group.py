from ..create_app import db
from datetime import datetime


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

    usuario_grupo = db.relationship(
        'usuario_grupo', backref="usuario")
