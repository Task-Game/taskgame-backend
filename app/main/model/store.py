from ..create_app import db
from datetime import datetime


class LojaTable(db.Model):
    __tablename__ = 'Loja'

    idLoja = db.Column(db.Integer,
                       primary_key=True)

    dataAbertura = db.Column(db.DateTime,
                             unique=False,
                             nullable=False,
                             default=datetime.now())

    dataFechamento = db.Column(db.DateTime,
                               unique=False,
                               nullable=False)

    item = db.relationship('Item', backref='loja')
    grupo = db.relationship('Grupo', backref='loja')


